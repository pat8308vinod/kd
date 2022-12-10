from django.urls import re_path as url
from django.conf.urls import include
from KeyDataService import views


urlpatterns=[
    
    url(r'^addKeyDetails/$', views.addKeyDetails),
    # url(r'^addGoogleAnalyticsData/$', views.addGoogleAnalyticsData),
  
]