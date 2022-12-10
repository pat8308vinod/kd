from django.db import models

from KeydabraManagerController.models import Report
from KeyDataService.models import KeyData
from ClientManagementService.models import Client
from SummaryDXIInsightService.models import Collateral

# Create your models here.
class ClientSitePage(models.Model):
    id = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientID')
    pageName = models.CharField(max_length=200, null=True)
    pageReferenceID = models.IntegerField(null =True)
    updatedDate = models.DateTimeField(auto_now_add=True, null=True)
    pageURL = models.CharField(max_length=400, null=True)
    class Meta:
        db_table = 'ClientSitePage'

class CustomerFlow(models.Model):
    id = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientID')
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    keyDataID = models.ForeignKey(KeyData, on_delete=models.CASCADE, db_column='keyDataID')
    reportName = models.CharField(max_length=50, default='ACDF')
    flowPercent = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    flowVisitors = models.IntegerField(null=True)
    flowRanking = models.IntegerField(null=True)
    class Meta:
        db_table = 'CustomerFlow'

class FlowPageOrder(models.Model):
    id = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID', default=1)
    customerFlowID = models.ForeignKey(CustomerFlow, on_delete=models.CASCADE, db_column='customerFlowID')
    clientSitePageID = models.ForeignKey(ClientSitePage, on_delete=models.CASCADE, db_column='clientSitePageID')
    reportName = models.CharField(max_length=50, default='ACDF')
    pageOrder = models.IntegerField(null=True)
    class Meta:
        db_table = 'FlowPageOrder'

class HeatMap(models.Model):
    id = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    clientSitePageID = models.ForeignKey(ClientSitePage, on_delete=models.CASCADE, db_column='clientSitePageID')
    reportName = models.CharField(max_length=50, default='ACDF')
    heatMapRank = models.IntegerField(null=True)
    collateralID = models.IntegerField(null=True)
    class Meta:
        db_table = 'HeatMap'

class FeatureType(models.Model):
    id = models.AutoField(primary_key=True)
    featureName = models.CharField(max_length=100, null=True)
    featureDefinition = models.CharField(max_length=800, null=True)
    featureUnit = models.CharField(max_length=20, null=True)
    class Meta:
        db_table = 'FeatureType'

class TopFeature(models.Model):
    id = models.AutoField(primary_key=True)
    featureID = models.ForeignKey(FeatureType, on_delete=models.CASCADE, db_column='featureID', default=2)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    featureDescription = models.CharField(max_length=500, null=True)
    significance = models.DecimalField(max_digits=50, decimal_places=3, null=True)
    clientSitePageID = models.ForeignKey(ClientSitePage, on_delete=models.SET_NULL, db_column='clientSitePageID', null=True)
    collateralID = models.ForeignKey(Collateral, on_delete=models.SET_NULL, db_column='collateralID', null=True)
    reportName = models.CharField(max_length=50, default='ACDF')
    class Meta:
        db_table = 'TopFeature'

class FeatureSuggestion(models.Model):
    ID = models.AutoField(primary_key=True)
    featureID = models.ForeignKey(FeatureType, on_delete=models.CASCADE, db_column='featureID')
    suggestionText = models.TextField(max_length=1000, null=True)
    class Meta:
        db_table = 'FeatureSuggestion'

class VisitorSegmentation(models.Model):
    ID = models.AutoField(primary_key=True)
    userID = models.TextField(max_length=1000, null=True)
    featureID = models.ForeignKey(FeatureType, on_delete=models.CASCADE, db_column='featureID')
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    reportName = models.CharField(max_length=50, default='ACDF')
    significance = models.DecimalField(max_digits=50, decimal_places=7, null=True)
    compositeDXI = models.DecimalField(max_digits=50, decimal_places=15, null=True)
    userRank = models.IntegerField(null=True)
    metaInfo = models.CharField(max_length=70, null=True)
    class Meta:
        db_table = 'VisitorSegmentation'