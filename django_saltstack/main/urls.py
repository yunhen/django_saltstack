# coding=utf-8

from django.conf.urls import patterns, include, url

from .views import TriggerSaltCommandView


urlpatterns = patterns(
    '',
    url(r'^$', TriggerSaltCommandView.as_view(), name='trigger_salt_command'),
)
