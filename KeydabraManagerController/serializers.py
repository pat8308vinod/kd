from rest_framework import serializers
from KeydabraManagerController.models import Report, ClientReportSchedule

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ClientReportScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientReportSchedule
        fields = '__all__'