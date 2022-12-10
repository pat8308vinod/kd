from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from KeydabraManagerController.models import Report
from KeyDataService.models import KeyData
from KeyDataService.serializers import KeyDataSerializer, GoogleAnalyticsDataSerializer
# Create your views here.
@api_view(['PUT'])
def updateCityDetails(request):
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        keydata = KeyData.objects.get(ID = request_data['keyDataID'])
        keydata_serializer = KeyDataSerializer(keydata, data=request.data)
        if keydata_serializer.is_valid():
            keydata_serializer.save()
            return Response(keydata_serializer.data)
        return Response(keydata_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addKeyDetails(request):
    if request.method == 'POST':
        city_data = JSONParser().parse(request)
        city_ser = KeyDataSerializer(data=city_data)
        if city_ser.is_valid():
            city_ser.save()
            return Response(city_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(city_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addGoogleAnalyticsData(request):
    if request.method == 'POST':
        analytics_data = JSONParser().parse(request)
        analytics_ser = GoogleAnalyticsDataSerializer(data=analytics_data)
        if analytics_ser.is_valid():
            analytics_ser.save()
            return Response(analytics_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(analytics_ser.errors, status=status.HTTP_400_BAD_REQUEST)

