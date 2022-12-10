from django.urls import re_path as url
from django.conf.urls import include
from ClientReportController import views


urlpatterns=[

    url(r'^getDashboardSummary/$', views.getDashboardSummary),    
    url(r'^getPredictionsAndPrescriptions/$', views.getPredictionsAndPrescriptions),
    url(r'^getKeyData/$', views.getKeyData),
    url(r'^getTransactionalInsights/$', views.getTransactionalInsights),
    url(r'^getVisualInsights/$', views.getVisualInsights),
    url(r'^getBehavioralInsights/$', views.getBehavioralInsights),
    url(r'^getClientReportDates/$', views.getClientReportDates),
    url(r'^getStandardSuggestions/$', views.getStandardSuggestions),
    url(r'^getVisitorInsights/$', views.getVisitorInsights),
]