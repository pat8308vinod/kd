from django.db import models
from SummaryDXIInsightService.models import Report

# Create your models here.
class KeyDataType(models.Model):
    ID = models.AutoField(primary_key=True)
    typeName = models.CharField(max_length=20)
    typeDescripption = models.CharField(max_length=35)
    class Meta:
        db_table = 'KeyDataType'


class KeyData(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    keyDataTypeID = models.ForeignKey(KeyDataType, on_delete=models.CASCADE, db_column='keyDataTypeID')
    reportName = models.CharField(max_length=50, default='ACDF')
    userCount = models.IntegerField(null=True)
    revenue = models.DecimalField(null=True, max_digits=10, decimal_places=3)
    conversionRate = models.DecimalField(null=True, max_digits=10, decimal_places=3)
    isApproved = models.BooleanField(null=True)
    approvedBy = models.CharField(null=True, max_length=50)
    name = models.CharField(max_length=35)
    class Meta:
        db_table = 'KeyData'


class GoogleAnalyticsData(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    parameterName = models.CharField(max_length=50)
    keyHeader = models.CharField(max_length=35, null=True)
    valueHeader = models.CharField(max_length=35, null=True)
    key = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=50, null=True)
    isApproved = models.BooleanField(null=True)
    approvedBy = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = 'GoogleAnalyticsData'

class Location(models.Model):
    ID = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    population = models.IntegerField(null=True)
    avgAge = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    avgIncome = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    countryCode =  models.CharField(max_length=15, null=True)
    class Meta:
        db_table = 'Location'

class SegmentationData(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    reportName = models.CharField(max_length=50, default='ACDF')
    segmentType = models.CharField(max_length=35, null=True)
    loosingScore = models.IntegerField(null=True)
    loyalScore = models.IntegerField(null=True)
    hibernatingScore = models.IntegerField(null=True)
    topScore = models.IntegerField(null=True)
    class Meta:
        db_table = 'SegmentationData'