from django.conf.urls import url
from FocusApp import views

urlpatterns = [
    url(r'^$', views.Index, name='news'),
    url(r'^(?P<article_id>[0-9]+)/$', views.News, name='article'),
    url(r'^(?P<article_id>[0-9]+)/comment/$', views.Comment_Article, name='comment'),
    url(r'^(?P<article_id>[0-9]+)/collect/$', views.Collect_Article, name='collect'),
    url(r'^(?P<article_id>[0-9]+)/thumbup/$', views.ThumbUp_Article, name='thumbup'),
]
