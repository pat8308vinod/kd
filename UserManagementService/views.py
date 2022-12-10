from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from AuthenticationService.serializers import UserCredentialsSerializer
from AuthenticationService.models import UserCredentials
from KeydabraAdminController.serializers import KeydabraUserSerializer

# Create your views here.
@api_view(['POST'])
def addUser(request):
    if request.method == 'POST':
        kduser_data = JSONParser().parse(request)
        kduser_serializer = KeydabraUserSerializer(data=kduser_data)
        if kduser_serializer.is_valid():
            kduser_serializer.save()
            return Response(kduser_serializer.data, status=status.HTTP_201_CREATED)
        return Response(kduser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def generateUserCredentials(request):
    if request.method=='GET':
        credentials = UserCredentials.objects.all()
        credentials_serializer = UserCredentialsSerializer(credentials, many=True)
        index, response_data = 0, {}
        for credential in credentials_serializer.data:
            response_data[index] = credential
            index += 1
        print(response_data)
        return Response(credentials_serializer.data)

    elif request.method=='POST':
        credential_data = JSONParser().parse(request)
        credential_serializer = UserCredentialsSerializer(data=credential_data)
        if credential_serializer.is_valid():
            credential_serializer.save()
            return Response(credential_serializer.data, status=status.HTTP_201_CREATED)
        return Response(credential_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT'])
def updateUserCredentials(request):
    if request.method=='PUT':
        credential_data = JSONParser().parse(request)
        credential = UserCredentials.objects.get(username = credential_data['username'])
        credential_serializer = UserCredentialsSerializer(credential, data = credential_data)
        if credential_serializer.is_valid():
            credential_serializer.save()
            return Response(credential_serializer.data)
        return Response(credential_serializer.errors, status=status.HTTP_400_BAD_REQUEST)