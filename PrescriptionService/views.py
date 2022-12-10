from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from SummaryDXIInsightService.models import Statements
from SummaryDXIInsightService.serializers import StatementsSerializer
from PrescriptionService.models import Prescription
from PrescriptionService.serializers import PrescriptionSerializer

# Create your views here.
@api_view(['POST'])
def addPrescription(request):
    if request.method == 'POST':
        statement_data = JSONParser().parse(request)
        statement_ser = PrescriptionSerializer(data=statement_data)
        if statement_ser.is_valid():
            statement_ser.save()
            return Response(statement_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(statement_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def getPrescriptions(request):
    if request.method=='POST':
        prediction_data = JSONParser().parse(request)
        predictions = Statements.objects.filter(reportID = prediction_data['reportID'], statementType='PRESC')
        index, response_data = 0, []
        for prediction in predictions:
            pred = {}
            pred['statementText'] = prediction.statementText
            response_data.append(pred)
        print(response_data)
        return Response(response_data)