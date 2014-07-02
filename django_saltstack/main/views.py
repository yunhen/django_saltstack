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


class TriggerSaltCommandView(FormView):
    form_class = KeyForm
    template_name = 'main/trigger_salt_command.html'

    def get_success_url(self):
        return reverse('trigger_salt_command')

    def form_valid(self, form):
        cmd = get_object_or_404(SaltCommand, key=form.cleaned_data['key'])
        return self.render_to_response(
            context={
                'task_id': cmd.run_async(),
                'cmd': cmd,
            }
        )
