from django.conf.urls import url
from users import views


urlpatterns = [
  # url(r'^success/$',views.register , name="register"),
  # url(r'^login/$',views.login,name="login"),
   url(r'^register/$',views.register,name='register'),
  # url(r'^logout/$',views.logout,name='logout'),
 #  url(r'^change_pwd/$',views.change,name='change'),
]