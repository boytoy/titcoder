from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CourseView, name='course'),
    url(r'^(?P<course_id>[0-9]+)/$', views.CoursePage, name='course_page'),
]
