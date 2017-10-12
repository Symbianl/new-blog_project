from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^article/$', views.article, name='article'),
   # url(r'^category/$', views.category, name='category'),
    url(r'^article/(?P<id>\d+)$',views.article,name='article'),
    url(r'^tag/$',views.tag,name='tag'),
    url(r'^message/$',views.message,name='message'),
    url(r'^search/$',views.search, name = "search"),
    url(r'^search1/$',views.search,name="search"),
    url(r'read/$',views.read,name='read'),
    url(r'404/$', views.error, name='error'),
  #  url(r'^index/$', views.logout, name='logout'),




 #   url(r'^comment/(?P<det_id>\d+)$', views.comment,name='comment'),


]
