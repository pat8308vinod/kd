from django.urls import re_path as url
from django.conf.urls import include
from SummaryDXIInsightService import views


urlpatterns=[
    url(r'^addAllSummary/$', views.addAllSummary),
    url(r'^updateConversionRate/$', views.updateConversionRate),
    url(r'^updateDXI/$', views.updateDXI),
    url(r'^updateTargetDXI/$', views.updateTargetDXI),
    url(r'^updateTargetConversionRate/$', views.updateTargetConversionRate),
    url(r'^updateProspectiveBuyers/$', views.updateProspectiveBuyers),
    url(r'^updateHighDXIConversionRate/$', views.updateHighDXIConversionRate),
    url(r'^updateLowDXIConversionRate/$', views.updateLowDXIConversionRate),
    url(r'^updateNetDollarRevenue/$', views.updateNetDollarRevenue),
    url(r'^getDXIInferences/$', views.getDXIInferences),
    url(r'^getHistoricalDXIInsights/$', views.getHistoricalDXIInsights),
]