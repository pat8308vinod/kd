from django.db import models
from KeydabraManagerController.models import Report
from SummaryDXIInsightService.models import Collateral
from ClientManagementService.models import Client

# Create your models here.
class TransactionSummary(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    reportName = models.CharField(max_length=50, default='ACDF')
    transactions = models.IntegerField(null=True)
    income = models.DecimalField(max_digits=50, decimal_places=3, null=True)
    itemsInPurchase = models.IntegerField(null=True)
    avgSizeOfPurchase = models.DecimalField(max_digits=50, decimal_places=3, null=True)
    # isApproved = models.BooleanField(null=True)
    # approvedBy = models.CharField(max_length=50)
    class Meta:
        db_table = 'TransactionSummary'

class Product(models.Model):
    ID = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientID')
    collateralID = models.ForeignKey(Collateral, on_delete=models.SET_NULL, db_column='collateralID', null=True)
    productName = models.TextField(max_length=500, null=True)
    productDesc = models.CharField(max_length=500, null=True)
    class Meta:
        db_table = 'Product'

class TopProduct(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    productID = models.ForeignKey(Product, on_delete=models.SET_NULL, db_column='productID', null=True)
    reportName = models.CharField(max_length=50, default='ACDF')
    # productName = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)
    class Meta:
        db_table = 'TopProduct'

class CNNRecommender(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    productID = models.ForeignKey(Product, on_delete=models.SET_NULL, db_column='productID', null=True)
    reportName = models.CharField(max_length=50, default='ACDF')
    class Meta:
        db_table = 'CNNRecommender'

class CNNSimilarProduct(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    sourceProdID = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='sourceProdID', null=True)
    recommendedProdID = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='recommendedProdID', null=True)
    similarityScore = models.DecimalField(max_digits=50, decimal_places=9, null=True)
    reportName = models.CharField(max_length=50, default='ACDF')
    class Meta:
        db_table = 'CNNSimilarProduct'

class MarketBasket(models.Model):
    ID = models.AutoField(primary_key=True)
    reportID = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='reportID')
    antecedentProdID = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='antecedentProdID', null=True)
    consequentProdID = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='consequentProdID', null=True)
    confidenceScore = models.DecimalField(max_digits=50, decimal_places=9, null=True)
    liftScore = models.DecimalField(max_digits=50, decimal_places=9, null=True)
    totalPrice = models.DecimalField(max_digits=50, decimal_places=9, null=True)
    combinationRank = models.IntegerField(null=True)
    sortingOrder = models.CharField(max_length=20, null=True)
    reportName = models.CharField(max_length=50)
    class Meta:
        db_table = 'MarketBasket'