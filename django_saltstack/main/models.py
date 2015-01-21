# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from uuidfield import UUIDField
import salt.client
from model_utils.models import TimeStampedModel
from adminsortable.models import Sortable

from .utils import notify_hipchat


class SaltCommand(Sortable):
    name = models.CharField(max_length=256)
    description = models.TextField()
    key = UUIDField(auto=True)
    salt_target = models.CharField(
        max_length=256,
        help_text=u'Regex for minion ids that will be targetted by the command')
    salt_function = models.CharField(
        max_length=256,
        help_text=u'Salt function to execute. E.g. "state.highstate"')
    hipchat_notification_msg = models.TextField(
        blank=True,
        null=True,
        help_text=u'Message that will be posted in hipchat when this key is triggered\
                use placeholder {cmd} for command and {id} for task_id')
    is_github_hook = models.BooleanField(
        default=False,
        help_text=u'If this is checked the command can only be triggered "github-style": https://developer.github.com/webhooks/')
    github_secret = UUIDField(auto=True)

    is_dockerhub_hook = models.BooleanField(
        default=False,
        help_text=u'If this is checked the command can only be triggered "dockerhub-style": https://docs.docker.com/docker-hub/repos/#webhooks')

    def run_async(self):
        client = salt.client.LocalClient()
        task_id = client.cmd_async(
            self.salt_target,
            self.salt_function,
            [a.value for a in self.saltarg_set.all()],
            ret=settings.DEFAULT_RETURNERS,
        )
        if self.hipchat_notification_msg:
            rendered_msg = self.hipchat_notification_msg.format(cmd=self, id=task_id)
            msg = '{msg} View state log on {saltobserver_url}/jobs/{id} after state has finished.'.format(
                saltobserver_url=settings.SALTOBSERVER_URL,
                msg=rendered_msg,
                id=task_id)
            notify_hipchat(msg)
            return task_id

    def get_absolute_url(self):
        if self.is_github_hook:
            return reverse('github_trigger_salt_command', kwargs={'key': str(self.key)})
        elif self.is_dockerhub_hook:
            return reverse('dockerhub_trigger_salt_command', kwargs={'key': str(self.key)})
        else:
            return reverse('trigger_salt_command')

    def __unicode__(self):
        return 'salt \'{}\' {} {}'.format(
            self.salt_target,
            self.salt_function,
            ' '.join([a.value for a in self.saltarg_set.all()])
        )

    class Meta(Sortable.Meta):
        pass


class SaltArg(Sortable):
    command = models.ForeignKey('main.SaltCommand')
    value = models.CharField(max_length=256)

    class Meta(Sortable.Meta):
        pass
