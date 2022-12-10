from django.urls import re_path as url
from django.conf.urls import include
from TransactionService import views


urlpatterns=[
    url(r'^addTopProduct/$', views.addTopProduct),
    url(r'^addTransactionSummary/$', views.addTransactionSummary),
    url(r'^getTransactionSummary/$', views.getTransactionSummary),
    url(r'^transactions/$',views.transactions,name="transactions"),
]