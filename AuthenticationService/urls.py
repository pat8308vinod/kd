from django.urls import re_path as url

# from django.conf.urls import url
from AuthenticationService import views



urlpatterns=[
    url(r'^login/$', views.loginApi),
    url(r'^signin/$', views.login),
]