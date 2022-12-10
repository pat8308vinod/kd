"""kdbackendapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.conf.urls import include
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^', include('accounts.urls')),
    url(r'^', include('UserManagementService.urls')),
    url(r'^', include('AuthenticationService.urls')),
    url(r'^', include('ClientManagementService.urls')),
    url(r'^', include('KeydabraAdminController.urls')),
    url(r'^', include('KeydabraManagerController.urls')),
    url(r'^', include('SummaryDXIInsightService.urls')),
    url(r'^', include('PredictionService.urls')),
    url(r'^', include('ClientReportController.urls')),
    url(r'^', include('RecommendationService.urls')),
    url(r'^', include('PrescriptionService.urls')),
    url(r'^', include('KeyDataService.urls')),
    url(r'^', include('TransactionService.urls')),
    url(r'^', include('VisualInsightService.urls')),
    url(r'^', include('BehavioralInsightService.urls')),
    url(r'^overview/$',overview,name="overview"),
    url(r'^suggestions/$',suggestions,name="suggestions"),
    url(r'^customers/$',customers,name="customers"),
    url(r'^visitors/$',visitors,name="visitors"),
     url(r'^glossary/$',glossary,name="glossary"),
    url(r'^si_report/$',si_report)
      
]

