# coding=utf-8

from django.conf.urls import patterns, include, url

from .views import TriggerSaltCommandView, GetTaskInfoView


urlpatterns = patterns(
    '',
    url(r'^$', TriggerSaltCommandView.as_view(), name='trigger_salt_command'),
    url(r'^(?P<task_id>\d+)/$', GetTaskInfoView.as_view(), name='get_task_info'),
)
