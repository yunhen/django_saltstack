# coding=utf-8
import hmac

from django.views.generic import (
    FormView, TemplateView, DetailView
)
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

# changes in 1.7: remove after upgrade
try:
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    from django.contrib.sites.models import get_current_site

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
        # verify this is not a github hook
        if self.object.is_github_hook:
            raise Http404()

        cmd = get_object_or_404(SaltCommand, key=form.cleaned_data['key'])
        task_id = cmd.run_async()
        context = self.get_context_data(self.kwargs)
        context.update({
            'task_id': task_id,
            'cmd': cmd,
        })
        return self.render_to_response(context)


class GithubTriggerSaltCommandView(DetailView):
    model = SaltCommand
    template_name = 'main/github_trigger_salt_command.html'
    http_method_names = [u'get', u'post']

    def get_object(self):
        return get_object_or_404(SaltCommand, key=self.kwargs['key'])

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # verify this is a github hook
        if not self.object.is_github_hook:
            raise Http404()

        # verify signature:
        # https://developer.github.com/v3/repos/hooks/#create-a-hook
        signature = request.META.get('HTTP_HUB_SIGNATURE')
        sig = hmac.new(str(self.object.github_secret), request.body)
        if not sig.hexdigest() == signature:
            raise PermissionDenied()

        task_id = self.object.run_async()

        context = self.get_context_data(object=self.object)
        context['task_id'] = task_id
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(GithubTriggerSaltCommandView, self).get_context_data(**kwargs)
        context['site'] = get_current_site(self.request)
        return context


class GetTaskInfoView(TemplateView):
    template_name = 'main/get_task_info.html'

    def get_context_data(self, **kwargs):
        context = super(GetTaskInfoView, self).get_context_data(**kwargs)
        print 'getting taskinfo...'
        context['output'] = get_task_info(self.kwargs['task_id'])
        print 'finished getting infos...'
        return context
