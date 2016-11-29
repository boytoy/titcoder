from django.conf.urls import url, include
from django.contrib import admin
from CourseApp import urls as CourseApp_urls
from CourseApp import views as CourseViews
from FocusApp import urls as FocusApp_urls
from BlogApp import urls as BlogApp_urls
from BBS import urls as BBS_urls
# from ChatApp import urls as Chat_urls
from grappelli import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', CourseViews.Index, name='index'),
    url(r'^course/', include(CourseApp_urls)),
    url(r'^news/', include(FocusApp_urls)),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^register/$', CourseViews.Register, name='register'),
    url(r'^login/$', CourseViews.Log_In, name='login'),
    url(r'^logout/$', CourseViews.Log_Out, name='logout'),
    url(r'^blog/', include(BlogApp_urls, namespace='blog', app_name='blog')),
    url(r'^bbs/', include(BBS_urls, namespace='bbs', app_name='bbs')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^chatroom/', include(Chat_urls)),
    # url(r'^course_page/', CourseViews.CoursePageView, name='course_page'),
    # url(r'^blog/', BlogViews.IndexView, name="index"),
    # url(r'^blog/', include(BlogApp_urls)),
    # url(r'^course/$', CourseViews.CourseView, name='course'),
    # url(r'^news/$', FocusViews.Index, name='news'),
    # url(r'^(?P<course_id>[0-9]+)/$', CourseViews.Course, name='article'),
    # url(r'^(?P<article_id>[0-9]+)/comment/$', FocusViews.Comment_Article, name='comment'),
    # url(r'^(?P<article_id>[0-9]+)/comment/$', FocusViews.Comment_Article, name='comment'),
    # url(r'^(?P<article_id>[0-9]+)/collect/$', FocusViews.Collect_Article, name='collect'),
    # url(r'^(?P<article_id>[0-9]+)/thumbup/$', FocusViews.ThumbUp_Article, name='thumbup'),
    # url(r'^(?P<article_id>[0-9]+)/$', FocusViews.News, name='article'),
]
