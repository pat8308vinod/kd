from rest_framework import serializers
from KeyDataService.models import KeyDataType, KeyData, SegmentationData, GoogleAnalyticsData


class KeyDataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyDataType
        fields = ('ID', 'typeName', 'typeDescripption')

class KeyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyData
        fields = (
            'ID', 'reportID', 'keyDataTypeID', 'userCount', 'revenue', 
            'conversionRate', 'isApproved', 'approvedBy', 'name'
        )

class GoogleAnalyticsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleAnalyticsData
        fields = (
            'ID', 'reportID', 'parameterName', 'keyHeader', 'valueHeader', 'key',
            'value', 'isApproved', 'approvedBy'
        )

class SegmentationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegmentationData
        fields = '__all__'