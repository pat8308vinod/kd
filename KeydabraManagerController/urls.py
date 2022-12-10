from django.urls import re_path as url
from django.conf.urls import include
from KeydabraManagerController import views


urlpatterns=[
    url(r'^addReport/$', views.addReport),
    url(r'^getReportDueDates/$', views.getReportDueDates),
    url(r'^viewAllReportMetaDataForClient/$', views.viewAllReportMetaDataForClient),
]