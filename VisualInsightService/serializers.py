from rest_framework import serializers
from VisualInsightService.models import ClientSitePage, CustomerFlow, FlowPageOrder, HeatMap, TopFeature
from VisualInsightService.models import FeatureSuggestion, VisitorSegmentation

class ClientSitePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSitePage
        fields = '__all__'

class CustomerFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFlow
        fields = '__all__'

class FlowPageOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowPageOrder
        fields = '__all__'

class HeatMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatMap
        fields = '__all__'

class TopFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopFeature
        fields = '__all__'

class FeatureSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureSuggestion
        fields = '__all__'

class VisitorSegmentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorSegmentation
        fields = '__all__'