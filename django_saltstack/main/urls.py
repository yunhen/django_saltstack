# coding=utf-8

from django.conf.urls import patterns, include, url

from .views import TriggerSaltCommandView, GithubTriggerSaltCommandView, GetTaskInfoView


urlpatterns = patterns(
    '',
    url(r'^$', TriggerSaltCommandView.as_view(), name='trigger_salt_command'),
    url(r'^github/(?P<key>\w+)/$',
        GithubTriggerSaltCommandView.as_view(),
        name='github_trigger_salt_command'),
    # url(r'^(?P<task_id>\d+)/$', GetTaskInfoView.as_view(), name='get_task_info'),
)
