from django.db import models
from KeydabraManagerController.models import Report

# Create your models here.
class SummaryInsights(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    month = models.CharField(max_length=15)
    DXI = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    TargetDXI = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    currentConversionRate = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    targetConversionRate = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    GAConversionRate = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    visitors = models.IntegerField(null=True)
    uniqueBuyers = models.IntegerField(null=True)
    transactions = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    prospectiveBuyers = models.IntegerField(null=True)
    netDollarValue = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    topDXIConversionRate = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    lowDXIConversionRate = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    BehavioralDXI = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    KPIDXI = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    TransactionalDXI = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    VisualDXI = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    bestSource = models.CharField(max_length=300, null=True)
    bestSeller = models.CharField(max_length=300, null=True)
    allAppDownloads = models.IntegerField(null=True)
    reportName = models.CharField(max_length=50, default='ACDF')
    class Meta:
        db_table = 'SummaryInsights'


class Statements(models.Model):
    statement_type_choices = [
        ('INFER', 'Inference'),
        ('OBSER', 'Observation'),
        ('PRED', 'Prediction'),
        ('RECOM', 'Recommendation'),
        ('INSIGHT', 'Insight'),
        ('PRESC', 'Prescription'),
        ('HEATMAP', 'Heatmap'),
        ('SENTIMENT', 'SentimentalAnalysis'),
    ]
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    statementType = models.CharField(max_length=10, choices=statement_type_choices)
    statementSubtype = models.CharField(max_length=10, null=True)
    informationType = models.CharField(max_length=30)
    statementText = models.TextField(max_length=500)
    solutionText = models.TextField(max_length=1000, null=True)
    isApproved = models.BooleanField(default=False)
    approvedBy = models.CharField(max_length=50)
    overviewFlag = models.BooleanField(default=False)
    reportName = models.CharField(max_length=50, default='ACDF')
    class Meta:
        db_table = 'Statements'

class Collateral(models.Model):
    id = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.SET_NULL, db_column='reportID', null=True)
    typeName = models.TextField(max_length=350, null=True)
    typeID = models.IntegerField(null=True)
    collateralMimeType = models.CharField(max_length=8)
    collateralContent = models.BinaryField()
    collateralName = models.CharField(max_length=400, null=True)
    class Meta:
        db_table = 'Collateral'