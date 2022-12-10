from django.db import models
from SummaryDXIInsightService.models import Statements

# Create your models here.
class Prescription(models.Model):
    ID = models.AutoField(primary_key=True)
    predictionID = models.ForeignKey(Statements, on_delete=models.SET_NULL, db_column='predictionID', null=True)
    reportForMonth = models.CharField(max_length=25, null=True)
    prescriptionName = models.TextField(null=True)
    prescriptionSection = models.CharField(max_length=25, null=True)
    prescriptionText = models.TextField(null=True)
    implementaionDate = models.DateField(null=True)
    implementationStatus = models.BooleanField(default=False)
    class Meta:
        db_table = 'Prescription'