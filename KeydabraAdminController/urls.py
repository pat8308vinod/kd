from django.urls import re_path as url
from django.conf.urls import include
from KeydabraAdminController import views


urlpatterns=[
    url(r'^viewActiveClients/$', views.viewActiveClients),
    url(r'^addClient/$', views.addClient),
    url(r'^enableClient/$', views.enableClient),
    url(r'^disableClient/$', views.disableClient),
    url(r'^addUserForClient/$', views.addUserForClient),
]