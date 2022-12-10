from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime as dt

from ClientManagementService.models import Client
from ClientManagementService.serializers import ClientSerializer
from KeydabraManagerController.serializers import ReportSerializer, ClientReportSchedule
from KeydabraManagerController.models import Report
from SummaryDXIInsightService.models import SummaryInsights

# Create your views here.
@api_view(['GET'])
def viewAllClients(request):
    if request.method=='GET':
        clients = Client.objects.all()
        clients_serializer = ClientSerializer(clients, many=True)
        index, response_data = 0, {}
        for client in clients_serializer.data:
            response_data[index] = client
            index += 1
        print(response_data)
        return Response(clients_serializer.data)


@api_view(['POST'])
def viewAllReportMetaDataForClient(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id = client_data.ID, forMonth=req_data['forMonth'])
        report_details = {
            'id': report_data.pk,
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod
        }
        print(report_details)
        summary = SummaryInsights.objects.get(reportID = report_data.pk)
        response_data = {
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod,
            'DXI': summary.DXI,
            'TargetDXI': summary.TargetDXI,
            'currentConversionRate': summary.currentConversionRate,
            'targetConversionRate': summary.targetConversionRate,
            'visitors': summary.visitors,
            'uniqueBuyers': summary.uniqueBuyers,
            'prospectiveBuyers': summary.prospectiveBuyers,
            'netDollarValue': summary.netDollarValue,
            'topDXIConversionRate': summary.topDXIConversionRate,
            'lowDXIConversionRate': summary.lowDXIConversionRate
        }

        # return Response(clients_serializer.data)
        return Response(response_data)


@api_view(['POST'])
def addReport(request, id = 0):
    if request.method == 'POST':
        report_data = JSONParser().parse(request)
        report_ser = ReportSerializer(data = report_data)
        if report_ser.is_valid():
            report_ser.save()
            return Response(report_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(report_ser._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getReportDueDates(request):
    if request.method=='GET':
        date_today = dt.today()
        schedules = ClientReportSchedule.objects.filter(deliveryDate__gte=date_today).order_by(
            'deliveryDate')[:10]
        clients = Client.objects.all()
        client_name_dict = dict()
        for client in clients:
            client_name_dict[client.ID] = client.companyName
        client_schedule_dict = dict()
        for schedule in schedules:
            client_name = client_name_dict[schedule.clientID.ID]
            delivery_date = schedule.deliveryDate
            publish_date = schedule.publishDate
            if client_name not in client_schedule_dict:
                client_schedule_dict[client_name] = {
                    'delivery_date': schedule.deliveryDate,
                    'publish_date': schedule.publishDate,
                    'draft_date': schedule.draftDate
                }
            print(schedule.clientID.ID, delivery_date, publish_date)
        return Response(client_schedule_dict)