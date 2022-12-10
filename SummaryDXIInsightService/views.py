from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from SummaryDXIInsightService.models import SummaryInsights, Statements
from SummaryDXIInsightService.serializers import SummaryInsightsSerializer

# Create your views here.
@api_view(['POST'])
def addAllSummary(request, id=0):
    if request.method == 'POST':
        summary_data = JSONParser().parse(request)
        summary_serializer = SummaryInsightsSerializer(data=summary_data)
        if summary_serializer.is_valid():
            summary_serializer.save()
            return Response(summary_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(summary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateConversionRate(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'currentConversionRate', summary_data['currentConversionRate'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateDXI(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'DXI', summary_data['DXI'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateTargetDXI(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'TargetDXI', summary_data['TargetDXI'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateTargetConversionRate(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'targetConversionRate', summary_data['targetConversionRate'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PATCH'])
# def updateHighDXI(request):
#     if request.method == 'PATCH':
#         summary_data = JSONParser().parse(request)
#         summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
#         setattr(summary, 'targetConversionRate', summary_data['targetConversionRate'])
#         # client['isEnabled'] = True
#         summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
#         if summary_ser.is_valid():
#             summary_ser.save()
#             return Response(summary_ser.data)
#         return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PATCH'])
# def updateLowDXI(request):
#     if request.method == 'PATCH':
#         summary_data = JSONParser().parse(request)
#         summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
#         setattr(summary, 'targetConversionRate', summary_data['targetConversionRate'])
#         # client['isEnabled'] = True
#         summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
#         if summary_ser.is_valid():
#             summary_ser.save()
#             return Response(summary_ser.data)
#         return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateProspectiveBuyers(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'prospectiveBuyers', summary_data['prospectiveBuyers'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateHighDXIConversionRate(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'topDXIConversionRate', summary_data['topDXIConversionRate'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateLowDXIConversionRate(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'lowDXIConversionRate', summary_data['lowDXIConversionRate'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def updateNetDollarRevenue(request):
    if request.method == 'PATCH':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        setattr(summary, 'netDollarValue', summary_data['netDollarValue'])
        # client['isEnabled'] = True
        summary_ser = SummaryInsightsSerializer(summary, data=summary_data, partial=True)
        if summary_ser.is_valid():
            summary_ser.save()
            return Response(summary_ser.data)
        return Response(summary_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def getDXISummaryInsights(request):
    if request.method == 'POST':
        summary_data = JSONParser().parse(request)
        summary = SummaryInsights.objects.get(reportID = summary_data['reportID'])
        insights = {
            'month': summary.month,
            'DXI': summary.DXI,
            'visitors': summary.visitors,
            'uniqueBuyers': summary.uniqueBuyers
        }
        return Response(insights)


@api_view(['POST'])
def getDXIInferences(request):
    if request.method=='POST':
        inference_data = JSONParser().parse(request)
        inferences = Statements.objects.filter(reportID = inference_data['reportID'], 
                        statementType='INFER', statementSubtype='DXI')
        # predictions_serializer = StatementsSerializer(predictions, many=True)
        response_data = []
        for inference in inferences:
            response_data.append(inference.statementText)
        print(response_data)
        # return Response(predictions_serializer.data)
        return Response(response_data)

@api_view(['GET'])
def getHistoricalDXIInsights(request):
    if request.method == 'GET':

        summary = SummaryInsights.objects.all()
        summary_serializer = SummaryInsightsSerializer(summary, many=True)
        # print(summary_serializer)
        return JsonResponse(summary_serializer.data, safe=False)