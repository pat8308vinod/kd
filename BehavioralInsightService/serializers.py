from rest_framework import serializers
from BehavioralInsightService.models import ReviewSentiment, WordCloud, ClusterData

class ReviewSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSentiment
        fields = '__all__'

class WordCloudSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordCloud
        fields = '__all__'

class ClusterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterData
        fields = '__all__'