from django.db import models

from ClientManagementService.models import Client

# Create your models here.
class Report(models.Model):
    ID = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientID')
    fromPeriod = models.DateField()
    toPeriod = models.DateField()
    forMonth = models.CharField(max_length=15)
    reportName = models.CharField(max_length=50, default=0)
    isApproved = models.BooleanField(null=True)
    isQADone = models.BooleanField(null=True)
    createdDate = models.DateField(null=True)
    updatedDate = models.DateField(auto_now_add=True)
    approvedDate = models.DateField(null=True)
    class Meta:
        db_table = 'Report'
        unique_together = (('ID', 'reportName'),)

class ClientReportSchedule(models.Model):
    ID = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientID')
    deliveryDate = models.DateField(null=True)
    draftDate = models.DateField(null=True)
    publishDate = models.DateField(null=True)
    class Meta:
        db_table = 'ClientReportSchedule'