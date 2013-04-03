# app specific urls
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url('^$', 'honbot.views.home'),
    url(r'^player/(?P<name>.*)/$', 'honbot.views.players'),
    url(r'^history/(?P<name>.*)/$', 'honbot.views.history'),
    url(r'^match/(?P<match_id>\d+)/$', 'honbot.views.match_view'),
    url(r'^chat/(?P<match_id>\d+)/$', 'honbot.views.chat_view'),
    (r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
)
