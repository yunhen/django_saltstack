# coding=utf-8

from django.conf.urls import patterns, include, url

from .views import TriggerSaltCommandView, GithubTriggerSaltCommandView, DockerHubTriggerSaltCommandView


urlpatterns = patterns(
    '',
    url(r'^$', TriggerSaltCommandView.as_view(), name='trigger_salt_command'),
    url(r'^github/(?P<key>\w+)/$',
        GithubTriggerSaltCommandView.as_view(),
        name='github_trigger_salt_command'),
    url(r'^dockerhub/(?P<key>\w+)/$',
        DockerHubTriggerSaltCommandView.as_view(),
        name='dockerhub_trigger_salt_command'),
)
