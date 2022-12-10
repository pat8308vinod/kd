from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from AuthenticationService.models import UserCredentials
from AuthenticationService.serializers import UserCredentialsSerializer
from ClientManagementService.models import Client, ClientUser
from KeydabraAdminController.models import KeydabraUser
from UserManagementService.models import User

# Create your views here.
@api_view(['GET', 'POST'])
def login(request,id=0):
    if request.method=='GET':
        userprofiles = UserCredentials.objects.all()
        userprofile_serializer = UserCredentialsSerializer(userprofiles, many=True)
        return Response(userprofile_serializer.data)

    elif request.method=='POST':
        userprofile_data = JSONParser().parse(request)
        userprofile = UserCredentials.objects.get(Email = userprofile_data['Email'])      
        user = {}
        try:
            clientprofile = ClientUser.objects.get(ID_id=userprofile.userID)
            client_data = Client.objects.get(ID = clientprofile.clientID.ID)
            if userprofile_data['Password'] == userprofile.password:
                user['id'] = userprofile.userID
                user['username'] = userprofile.username
                user['firstName'] = clientprofile.firstName
                user['lastName'] = clientprofile.lastName
                user['company'] = client_data.companyName
                return Response(user)
            else:
                return Response('Failed to login...', status=status.HTTP_400_BAD_REQUEST)
        except ClientUser.DoesNotExist:
            kduserprofile = KeydabraUser.objects.get(ID_id=userprofile.userID)
            if userprofile_data['Password'] == userprofile.password:
                user['id'] = userprofile.userID
                user['username'] = userprofile.username
                user['firstName'] = kduserprofile.firstName
                user['lastName'] = kduserprofile.lastName
                user['company'] = 'Keydabra'
                return Response(user)
            else:
                return Response('Failed to login...', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def loginApi(request):
        if request.method=='POST':
            request_data = JSONParser().parse(request)
            user_profile = User.objects.get(email = request_data['Email'])
            print('users:', user_profile)  
            user_data = {}
            try:
                client_data = Client.objects.get(ID = user_profile.clientID.ID)
                if request_data['Password'] == user_profile.password:
                    user_data['firstName'] = user_profile.firstName
                    user_data['lastName'] = user_profile.lastName
                    user_data['company'] = client_data.companyName
                    user_data['editFlag'] = user_profile.editFlag
                    user_data['isDevelopment'] = user_profile.isDevelopment
                    return Response(user_data)
                else:
                    return Response('Failed to login...', status=status.HTTP_400_BAD_REQUEST)
            except Client.DoesNotExist:
                return Response('Failed to login...', status=status.HTTP_400_BAD_REQUEST)