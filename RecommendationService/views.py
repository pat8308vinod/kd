from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from SummaryDXIInsightService.models import Statements
from SummaryDXIInsightService.serializers import StatementsSerializer

# Create your views here.
@api_view(['POST'])
def getAllRecommendations(request):
    if request.method=='POST':
        prediction_data = JSONParser().parse(request)
        recommendations = Statements.objects.filter(reportID=prediction_data['reportID'], statementType='RECOM')
        response_data = []
        for recommendation in recommendations:
            recom_dict = {}
            recom_dict['statementText'] = recommendation.statementText
            recom_dict['solutionText'] = recommendation.solutionText
            # recom_dict['referenceImage'] = recommendation.referenceImage
            response_data.append(recom_dict)
        print(response_data)
        return Response(response_data)


@api_view(['PATCH'])
def updateRecommendation(request):
    if request.method == 'PATCH':
        request_data = JSONParser().parse(request)
        prediction = Statements.objects.get(ID=request_data['ID'], statementType='RECOM')
        
        setattr(prediction, 'referenceImage', request_data['referenceImage'])
        print('Recommendation id:', request_data['ID'])
        prediction_ser = Statements(prediction, data=request_data, partial=True)
        if prediction_ser.is_valid():
            prediction_ser.save()
            return Response(prediction_ser.data)
        return Response(prediction_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addRecommendation(request):
    if request.method == 'POST':
        recommendation_data = JSONParser().parse(request)
        recommendation_ser = StatementsSerializer(data=recommendation_data)
        if recommendation_ser.is_valid():
            recommendation_ser.save()
            return Response(recommendation_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(recommendation_ser.errors, status=status.HTTP_400_BAD_REQUEST)