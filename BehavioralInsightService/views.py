from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from KeydabraManagerController.models import Report
from BehavioralInsightService.models import ClusterData

from BehavioralInsightService.serializers import WordCloudSerializer, ReviewSentimentSerializer

# Create your views here.
@api_view(['POST'])
def addWordCloudData(request):
    if request.method == 'POST':
        wordcloud_data = JSONParser().parse(request)
        wordcloud_serializer = WordCloudSerializer(data=wordcloud_data)
        if wordcloud_serializer.is_valid():
            wordcloud_serializer.save()
            return Response(wordcloud_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(wordcloud_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addReviewSentimentData(request):
    if request.method == 'POST':
        sentiment_data = JSONParser().parse(request)
        sentiment_serializer = ReviewSentimentSerializer(data=sentiment_data)
        if sentiment_serializer.is_valid():
            sentiment_serializer.save()
            return Response(sentiment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sentiment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def behavior(request):
    clientID = request.session['clientID']
    report_id = list(Report.objects.filter(clientID = clientID ).values_list('ID',flat=True))
    if len(report_id)>0:
        keydata_browser = list(ClusterData.objects.values().filter(keyDataTypeID = 2 , reportID = report_id[-1] ))
        keydata_city = list(ClusterData.objects.values().filter(keyDataTypeID = 1 , reportID = report_id[-1] ))
        keydata_os = list(ClusterData.objects.values().filter(keyDataTypeID = 3 , reportID = report_id[-1] ))
        keydata_device = list(ClusterData.objects.values().filter(keyDataTypeID = 5 , reportID = report_id[-1] ))
        keydata_channel = list(ClusterData.objects.values().filter(keyDataTypeID = 4 , reportID = report_id[-1] ))
        keydata_social = list(ClusterData.objects.values().filter(keyDataTypeID = 6 , reportID = report_id[-1] ))
        print("Browser list")   
        return render(request,"behavior.html",{'keydata_browser':keydata_browser,'keydata_city':keydata_city,'keydata_os':keydata_os,'keydata_device':keydata_device,'keydata_channel':keydata_channel,'keydata_social':keydata_social})
    else:
        return render(request,"behavior.html",{})   