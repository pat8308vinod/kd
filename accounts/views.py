
from certifi import where
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from rest_framework.response import Response
from ClientManagementService.models import Client, ClientUser
from SummaryDXIInsightService.models import SummaryInsights
from KeydabraManagerController.models import Report
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from accounts.models import UserProfile
from KeyDataService.models import KeyData,SegmentationData
from BehavioralInsightService.models import ClusterData
from accounts.serializers import UserProfileSerializer
from UserManagementService.models import User
from datetime import datetime

from django.contrib.auth import authenticate, login, logout


def loginform(request):
    return render(request,"login.html",{})
  

def login_user(request):
    if  request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user_profile = User.objects.get(email = email)if User.objects.filter(email = email ).exists() else True
            if user_profile == True:
              msg = 'Invalid Credential...!'
              return render(request,'login.html', {'msg':msg})
            #print('users:', user_profile)  
            user_data = {}
            client_data = Client.objects.get(ID = user_profile.clientID.ID)
            
            
            #report_list=list(Report.objects.filter(clientID = client_data.ID ))
            #current_reportData=report_list[-1]
            month_list = list(Report.objects.filter(clientID = client_data.ID ).values_list('forMonth','ID').order_by('-ID'))
            print("**********month_list**************")
            #print(month_list)

            #print(month_list)
            #print(insight_data)
            request.session['month'] =month_list    
            all_month = request.session['month']
            print(all_month)
            print("************************")
            month_list1 = []
            content = {}
            for result in month_list:
                content = {'id': result[1], 'month': result[0]}
                month_list1.append(content)
            print(month_list1)
            request.session['month1'] =month_list1   


            request.session['clientID'] = client_data.ID
            clientID = request.session['clientID']
           
            if user_profile and request.POST['email'] == user_profile.email and request.POST['password'] == user_profile.password:
               request.session['firstName'] = user_profile.firstName
               request.session['companyName'] = client_data.companyName
               request.session['subscription'] = client_data.subscription
               #request.session['fromPeriod'] = current_reportData
               #request.session['toPeriod'] = current_reportData.toPeriod


             
               subscription = request.session['subscription']
             
               if subscription == 'Premium':
                sub_text='Expert'
                request.session['sub_text'] =sub_text
               elif subscription == 'Standard':
                 sub_text='Premium'
                 request.session['sub_text'] =sub_text
               elif subscription == 'Basic':
                 sub_text='Standard'
                 request.session['sub_text'] =sub_text 



               return redirect('/overview')
            else:
                msg = 'Invalid Credential...!'
                return render(request,"login.html",{'msg':msg})
        except Client.DoesNotExist:
            return Response('Failed to login...', status=status.HTTP_400_BAD_REQUEST)

def logout(request):
    try:
        del request.session['subscription']
        
    except KeyError:
        pass
    return redirect('login')
        
# Create your views here.
@api_view(['GET', 'POST'])
def loginApi(request,id=0):
    if request.method=='GET':
        userprofiles = UserProfile.objects.all()
        userprofile_serializer = UserProfileSerializer(userprofiles, many=True)
        return JsonResponse(userprofile_serializer.data, safe=False)

    elif request.method=='POST':
        userprofile_data = JSONParser().parse(request)
        userprofile = UserProfile.objects.get(Email = userprofile_data['Email'])
        print(userprofile.UserId)
        if userprofile_data['Password'] == userprofile.Password:
            user = {
                'id': userprofile.UserId,
                'username': userprofile.UserName,
                'firstName': userprofile.FirstName,
                'lastName': userprofile.LastName
            }
            return JsonResponse(user, safe=False)
        else:
            return JsonResponse('Failed to login...', safe=False)