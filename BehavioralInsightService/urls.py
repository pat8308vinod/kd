from django.urls import re_path as url
from django.conf.urls import include
from BehavioralInsightService import views


urlpatterns=[
    url(r'^addWordCloudData/$', views.addWordCloudData),
    url(r'^addReviewSentimentData/$', views.addReviewSentimentData),
    url(r'^behavior',views.behavior,name="behavior"),
]