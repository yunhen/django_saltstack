# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

from uuidfield import UUIDField
import salt.client
from model_utils.models import TimeStampedModel
from adminsortable.models import Sortable


class SaltCommand(TimeStampedModel):
    name = models.CharField(max_length=256)
    description = models.TextField()
    key = UUIDField(auto=True)
    salt_target = models.CharField(
        max_length=256,
        help_text=u'Regex for minion ids that will be targetted by the command')
    salt_function = models.CharField(
        max_length=256,
        help_text=u'Salt function to execute. E.g. "state.highstate"')

    def run(self):
        client = salt.client.LocalClient()
        return client.cmd(
            self.salt_target,
            self.salt_function,
            [a.value for a in self.saltarg_set.all()]
        )

    def __unicode__(self):
        return 'salt \'{}\' {} {}'.format(
            self.salt_target,
            self.salt_function,
            ' '.join([a.value for a in self.saltarg_set.all()])
        )


class SaltArg(Sortable):
    command = models.ForeignKey('main.SaltCommand')
    value = models.CharField(max_length=256)

    class Meta(Sortable.Meta):
        pass