from rest_framework import serializers
from TransactionService.models import TransactionSummary, Product, TopProduct, CNNRecommender, CNNSimilarProduct


class TransactionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSummary
        fields = (
            'ID', 'reportID', 'transactions', 'income', 'itemsInPurchase', 
            'avgSizeOfPurchase', 'isApproved', 'approvedBy'
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProduct
        fields = (
            'ID', 'reportID', 'productName', 'quantity'
        )

class CNNRecommenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNNRecommender
        fields = '__all__'

class CNNSimilarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNNSimilarProduct
        fields = (
            'ID', 'reportID', 'sourceProdID', 'recommendedProdID', 'similarityScore'
        )