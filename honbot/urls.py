# app specific urls
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url('^$', 'honbot.views.home'),
    url(r'^player/(?P<name>.*)/$', 'honbot.player.players'),  # ranked player stats
    url(r'^c/player/(?P<name>.*)/$', 'honbot.player.players'),  # casual player stats
    url(r'^p/player/(?P<name>.*)/$', 'honbot.player.players'),  # public player stats
    url(r'^history/(?P<name>.*)/$', 'honbot.views.history'),  # redirect history to player page
    url(r'^banner/(?P<name>.*)/$', 'honbot.views.banner_view'),
    url(r'^match/(?P<match_id>[0-9]+)/$', 'honbot.views.match_view'),
    url(r'^builds/(?P<match_id>[0-9]+)/$', 'honbot.builds.build'),
    url(r'^chat/(?P<match_id>[0-9]+)/$', 'honbot.chat.chat'),
    url(r'^advanced/(?P<match_id>[0-9]+)/$', 'honbot.views.adv'),
    url(r'^avatar/(?P<number>[0-9]+)/$', 'honbot.avatar.avatar'),
    url(r'^match_history/(?P<number>[0-9]+)/$', 'honbot.match_history.history'),
    url(r'^recent/$', 'honbot.recent.recent'),
    (r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt")),
)
