# coding=utf-8
from django.views.generic import (
    FormView, TemplateView
)
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect

from braces.views import LoginRequiredMixin

from .forms import KeyForm
from .models import SaltCommand
from .utils import notify_hipchat, get_task_info


class TriggerSaltCommandView(FormView):
    form_class = KeyForm
    template_name = 'main/trigger_salt_command.html'

    def get_success_url(self):
        return reverse('trigger_salt_command')

    def form_valid(self, form):
        cmd = get_object_or_404(SaltCommand, key=form.cleaned_data['key'])
        task_id = cmd.run_async()
        if cmd.hipchat_notification_msg:
            notify_hipchat(cmd.hipchat_notification_msg.format(
                cmd=cmd, id=task_id))
        return self.render_to_response(
            context={
                'task_id': task_id,
                'cmd': cmd,
            }
        )


class GetTaskInfoView(TemplateView):
    template_name = 'main/get_task_info.html'

    def get_context_data(self, **kwargs):
        context = super(GetTaskInfoView, self).get_context_data(**kwargs)
        print 'getting taskinfo...'
        context['output'] = get_task_info(self.kwargs['task_id'])
        print 'finished getting infos...'
        return context
