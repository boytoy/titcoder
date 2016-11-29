from django.conf.urls import url
from BBS import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^article/(\d+)/$',views.article_detail,name='article_detail'),
    # url(r'~article/new/$',views.new_article,name='new_article'),
    # url(r'^article/new/$',views.new_article,name='new_article'),
    url(r'^account/logout/',views.acc_logout,name='logout'),
    url(r'^account/login/',views.acc_login,name='login'),
    url(r'new_article/', views.new_article, name="new_article"),
]
