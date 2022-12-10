
from certifi import where
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from ClientManagementService.models import Client, ClientUser
from SummaryDXIInsightService.models import SummaryInsights
from KeydabraManagerController.models import Report
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
from UserManagementService.models import User
from datetime import datetime

from django.contrib.auth import authenticate, login, logout


def loginform(request):
    #return HttpResponse("<h1>This is About Page</h1>")
    return render(request,"login.html",{})

def login_user(request):
    if  request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user_profile = User.objects.get(email = email)
            #print('users:', user_profile)  
            user_data = {}
            client_data = Client.objects.get(ID = user_profile.clientID.ID)
            report_data = list(Report.objects.filter(clientID = client_data.ID ))
            report_data_current=report_data[-1]
            insight_data= (SummaryInsights.objects.get(reportID = report_data_current.ID))
            report_data_current1=report_data[-2]
            insight_data1= (SummaryInsights.objects.get(reportID = report_data_current1.ID))
            month_list = list(Report.objects.filter(clientID = client_data.ID ).values_list('forMonth','ID').order_by('-ID'))
            print("**********month_list**************")
            print(month_list)
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
        
            if user_profile and request.POST['email'] == user_profile.email and request.POST['password'] == user_profile.password:
               request.session['firstName'] = user_profile.firstName
               request.session['companyName'] = client_data.companyName
               request.session['subscription'] = client_data.subscription
               return render(request,"dashboard.html",{'client_data':client_data, 'user_profile':user_profile,'report_data':report_data,'insight_data':insight_data,'insight_data1':insight_data1})
            else:
                 return render(request,"login.html")
        except Client.DoesNotExist:
            return Response('Failed to login...', status=status.HTTP_400_BAD_REQUEST)
   
        
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


            seg_list = list()
    featureName_list = list()
    content2 = {}
    for i,v in enumerate(v_seg):
        fid= v_seg[i]['featureID_id']

        seg_list.append(fid)
    print(seg_list)
    for i,f in enumerate(seg_list):
        f_name=list(FeatureType.objects.filter(id = f).values())
        content2 = {'obj': f_name}
        featureName_list.append(content2)
    print(featureName_list)    






















            
               /* Report Wise Change Suggestion table Data*/
               $('#s_tr').empty()
      

               for (let k = 0; k < f_type.length; k++) {
                 
                 
                  for (var i = 0; i < s_list.length; i++) 
                  {
                     for (var j = 0; j < s_list[i].length; j++) 
                     
                     {
                        if (s_list[i][j].featureID_id == f_type[k].id) 
                        {
                           $('#s_tr').append('<tr class="border bg-white"><td class="border">' + f_type[k].featureName + '</td><td class="ts"><li class="">' + s_list[i][j].suggestionText + '</li></td></tr>');
                        }
                        
                     }
                  }
               }
               /* End Report Wise Change Suggestion table Data*/