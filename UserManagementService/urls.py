from django.urls import re_path as url
from django.conf.urls import include
from UserManagementService import views

urlpatterns=[

    url(r'^addUser/$', views.addUser),
    url(r'^createUser/$', views.generateUserCredentials),
]