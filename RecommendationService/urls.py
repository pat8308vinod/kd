from django.urls import re_path as url
from django.conf.urls import include
from RecommendationService import views


urlpatterns=[
    url(r'^updateRecommendation/$', views.updateRecommendation),
    url(r'^addRecommendation/$', views.addRecommendation),
    url(r'^getAllRecommendations/$', views.getAllRecommendations),
]