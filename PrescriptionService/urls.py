from django.urls import re_path as url
from django.conf.urls import include
from PrescriptionService import views


urlpatterns=[

    url(r'^addPrescription/$', views.addPrescription),
    url(r'^getPrescriptions/$', views.getPrescriptions),
]