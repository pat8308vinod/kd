from django.urls import re_path as url
from django.conf.urls import include
from VisualInsightService import views


urlpatterns=[
    url(r'^addClientSitePage/$', views.addClientSitePage),
    url(r'^addHeatMap/$', views.addHeatMap),
    url(r'^addCustomerFlow/$', views.addCustomerFlow),
    url(r'^addFlowPageOrder/$', views.addFlowPageOrder),
    url(r'^addTopFeature/$', views.addTopFeature),
]