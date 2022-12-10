from rest_framework import serializers
from SummaryDXIInsightService.models import SummaryInsights, Statements, Collateral,Report


class SummaryInsightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryInsights
        fields = '__all__'

class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = '__all__'

class CollateralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collateral
        fields = '__all__'
        

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
