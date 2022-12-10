from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from ClientManagementService.serializers import ClientSerializer
from ClientManagementService.models import Client

# Create your views here.
@api_view(['POST'])
def addClient(request, id = 0):
    if request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_ser = ClientSerializer(data=client_data)
        if client_ser.is_valid():
            client_ser.save()
            return Response(client_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(client_ser._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def enableClient(request):
    if request.method == 'PATCH':
        client_data = JSONParser().parse(request)
        client = Client.objects.get(companyName=client_data['companyName'])
        setattr(client, 'isEnabled', True)
        client_ser = ClientSerializer(client, data=client_data, partial=True)
        if client_ser.is_valid():
            client_ser.save()
            return Response(client_ser.data)
        return Response(client_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def disableClient(request):
    if request.method == 'PATCH':
        client_data = JSONParser().parse(request)
        client = Client.objects.get(companyName=client_data['companyName'])
        setattr(client, 'isEnabled', False)
        client_ser = ClientSerializer(client, data=client_data, partial=True)
        if client_ser.is_valid():
            client_ser.save()
            return Response(client_ser.data)
        return Response(client_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def removeClient(request):
    client_data = JSONParser().parse(request)
    try:
        client = Client.objects.get(companyName=client_data['companyName'])
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)