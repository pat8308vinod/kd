from django.urls import re_path as url
from django.conf.urls import include
from PredictionService import views


urlpatterns=[
    url(r'^addPrediction/$', views.addPrediction),
    url(r'^getPredictions/$', views.getPredictions),
    url(r'^updatePredictions/$', views.updatePredictions),
    url(r'^addInsightForPrediction/$', views.addInsightForPrediction),
    url(r'^getAllInsightsForPredictions/$', views.getAllInsightsForPredictions),
    url(r'^updateInsightsForPrediction/$', views.updateInsightsForPrediction),
    url(r'^removeInsightForPrediction/$', views.removeInsightForPrediction),
    url(r'^getAllInferencesForDXI/$', views.getAllInferencesForDXI),
]