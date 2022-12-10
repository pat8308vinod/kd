from django.db import models
from KeydabraManagerController.models import Report
from KeyDataService.models import KeyDataType

# Create your models here.
class ReviewSentiment(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    reportName = models.CharField(max_length=50, default='ACDF')
    positiveScore = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    negativeScore = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    neutralScore = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    class Meta:
        db_table = 'ReviewSentiment'

class WordCloud(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    reportName = models.CharField(max_length=50, default='ACDF')
    text = models.TextField(null=True)
    frequency = models.IntegerField(null=True)
    metaInfo = models.CharField(max_length=35, null=True)
    class Meta:
        db_table = 'WordCloud'

class ClusterData(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    keyDataTypeID = models.ForeignKey(KeyDataType, on_delete=models.CASCADE, db_column='keyDataTypeID')
    reportName = models.CharField(max_length=50, default='ACDF')
    name = models.CharField(null=True, max_length=50)
    score= models.DecimalField(max_digits=50, decimal_places=3, null=True)
    metaInfo = models.CharField(max_length=35, null=True, default='Good Cluster')
    class Meta:
        db_table = 'ClusterData'