from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from ClientManagementService.models import Client
from ClientManagementService.serializers import ClientSerializer, ClientUserSerializer

# Create your views here.


@api_view(['GET'])
def viewActiveClients(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        response_data = []
        for client in clients:
            if client.isActive:
                client_dict = dict()
                client_dict[client.companyName] = {
                    'isEnabled': client.isEnabled,
                    'isActive': client.isActive,
                    'isEcommerce': client.isEcommerce,
                    'isLite': client.isLite,
                    'isPro': client.isPro
                }
                response_data.append(client_dict)
        print('No. of clients:', len(clients))
        return Response(response_data)


@api_view(['POST'])
def addClient(request, id=0):
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
        # client['isEnabled'] = True
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
        # client['isEnabled'] = False
        setattr(client, 'isEnabled', False)
        client_ser = ClientSerializer(client, data=client_data, partial=True)
        if client_ser.is_valid():
            client_ser.save()
            return Response(client_ser.data)
        return Response(client_ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addUserForClient(request):
    if request.method == 'POST':
        clientuser_data = JSONParser().parse(request)
        clientuser_ser = ClientUserSerializer(data=clientuser_data)
        if clientuser_ser.is_valid():
            clientuser_ser.save()
            return Response(clientuser_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(clientuser_ser._errors, status=status.HTTP_400_BAD_REQUEST)
