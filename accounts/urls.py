from django.urls import re_path as url
from accounts import views


urlpatterns=[
    url(r'^userlogin/$', views.loginform,name="login"),
    url(r'^login/$', views.loginApi),
    url('^login_user/$', views.login_user, name= 'loginuser'),
    url('^logout/$', views.logout, name= 'logout')
   
]