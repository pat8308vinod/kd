import re
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from SummaryDXIInsightService.models import Statements
from SummaryDXIInsightService.serializers import StatementsSerializer
from ClientManagementService.models import Client
from KeydabraManagerController.models import Report

# Create your views here.
@api_view(['POST'])
def getPredictions(request):
    if request.method=='POST':
        prediction_data = JSONParser().parse(request)
        predictions = Statements.objects.filter(reportID = prediction_data['reportID'], statementType='PRED')
        response_data = []
        for prediction in predictions:
            pred = {}
            pred['statementText'] = prediction.statementText
            pred['solutionText'] = prediction.solutionText
            response_data.append(pred)
        print(response_data)
        return Response(response_data)


@api_view(['PATCH'])
def updatePredictions(request):
    if request.method == 'PATCH':
        request_data = JSONParser().parse(request)
        prediction = Statements.objects.get(ID = request_data['ID'], statementType='PRED')
        print(request_data)
        if 'statementText' in request_data:
            setattr(prediction, 'statementText', request_data['statementText'])
        if 'solutionText' in request_data:
            setattr(prediction, 'solutionText', request_data['solutionText'])
        prediction_ser = StatementsSerializer(prediction, data=request_data, partial=True)
        if prediction_ser.is_valid():
            prediction_ser.save()
            return Response(prediction_ser.data)
        return Response(prediction_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def removePredictions(request):
    prediction_data = JSONParser().parse(request)
    try:
        pred = Statements.objects.get(prediction = prediction_data['ID'])
        pred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addInsightForPrediction(request):
    if request.method == 'POST':
        statement_data = JSONParser().parse(request)
        statement_ser = StatementsSerializer(data=statement_data)
        if statement_ser.is_valid():
            statement_ser.save()
            return Response(statement_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(statement_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def getAllInsightsForPredictions(request):
    if request.method == 'POST':
        req_data = JSONParser().parse(request)
        
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])
        
        insights = Statements.objects.filter(
            reportID=report_data.ID, statementType='INSIGHT', statementSubtype='Prediction'
        )
        response_data = list()
        for insight in insights:
            insight_dict = dict()
            insight_dict['insight_id'] = insight.ID
            insight_dict['insight_txt'] = insight.statementText
            response_data.append(insight_dict)
        
        print(insights)
        return Response(response_data)


@api_view(['PATCH'])
def updateInsightsForPrediction(request):
    if request.method == 'PATCH':
        request_data = JSONParser().parse(request)
        insight = Statements.objects.get(ID = request_data['insight_id'])
        setattr(insight, 'statementText', request_data['insight_txt'])
        insight_ser = StatementsSerializer(insight, data=request_data, partial=True)
        if insight_ser.is_valid():
            insight_ser.save()
            return Response(insight_ser.data)
        return Response(insight_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def removeInsightForPrediction(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        try:
            insight = Statements.objects.get(ID = request_data['insight_id'])
            print('insight.ID: ', insight.ID)
        except Statements.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        insight.delete()
        print('Successfully removed insight ', insight.ID)
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def addPrediction(request):
    if request.method == 'POST':
        statement_data = JSONParser().parse(request)
        statement_ser = StatementsSerializer(data=statement_data)
        if statement_ser.is_valid():
            statement_ser.save()
            return Response(statement_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(statement_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def getAllInferencesForDXI(request):
    if request.method == 'POST':
        req_data = JSONParser().parse(request)
        
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])
        
        insights = Statements.objects.filter(
            reportID=report_data.ID, statementType='INFER', statementSubtype='DXI'
        )
        response_data = list()
        for insight in insights:
            insight_dict = dict()
            insight_dict['insight_id'] = insight.ID
            insight_dict['insight_txt'] = insight.statementText
            response_data.append(insight_dict)
        
        print(insights)
        return Response(response_data)