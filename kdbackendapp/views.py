from django.shortcuts import render
from accounts.models import UserProfile
from django.http.response import JsonResponse,json
from django.http import HttpResponse
from rest_framework.response import Response
from KeydabraManagerController.models import Report
from SummaryDXIInsightService.models import SummaryInsights, Statements,Collateral
from VisualInsightService.models import TopFeature,FeatureSuggestion,FeatureType,VisitorSegmentation
from BehavioralInsightService.models import ClusterData
from KeyDataService.models import KeyData,SegmentationData
from TransactionService.models import TransactionSummary,TopProduct,Product,MarketBasket,CNNSimilarProduct
from django.db.models import Sum
from django.db.models import Q
from base64 import b64encode

def overview(request):
    clientID = request.session['clientID']
    report_data = list(Report.objects.filter(clientID = clientID ))
    print("*************       report_data             ***************")
    print(len(report_data))
    if len(report_data)>0:
        report_data_current=report_data[-1]
        insight_data= (SummaryInsights.objects.get(reportID = report_data_current.ID))
        report_data = list(Report.objects.filter(clientID = clientID ))
        
        Insightslist2 = []
        content1 = {}
        i=0
        while i< len(report_data):
            insight_data5= (SummaryInsights.objects.get(reportID = report_data[i].ID))
            content1 = {'obj': insight_data5}
            Insightslist2.append(content1)
            i=i+1
        print(Insightslist2[0]['obj'].ID)
        #return HttpResponse("<h1>This is About Page</h1>")
        report_id = list(Report.objects.filter(clientID = clientID ).values_list())
        keydata_channel = list(KeyData.objects.values().filter(keyDataTypeID = 4 , reportID = report_id[-1] ))
        keydata_browser = list(KeyData.objects.values().filter(keyDataTypeID = 2 , reportID = report_id[-1] ))
        keydata_os = list(KeyData.objects.values().filter(keyDataTypeID = 3 , reportID = report_id[-1] ))
        keydata_device = list(KeyData.objects.values().filter(keyDataTypeID = 5 , reportID = report_id[-1] ))
        histogram_img = Collateral.objects.values().get(reportID = report_data_current.ID , typeName = 'Composite DXI histogram' ) if Collateral.objects.filter(reportID = report_data_current.ID , typeName = 'Composite DXI histogram').exists() else False
        if histogram_img == False:
          msg = 'No Data Found'
          return render(request,"dashboard.html",{'insight_data':insight_data,'Insightslist2':Insightslist2,'keydata_browser':keydata_browser,'keydata_channel':keydata_channel,'keydata_os':keydata_os,'keydata_device':keydata_device,'msg':msg})
        else:
            image = b64encode(histogram_img['collateralContent']).decode("utf-8")
            return render(request,"dashboard.html",{'insight_data':insight_data,'Insightslist2':Insightslist2,'keydata_browser':keydata_browser,'keydata_channel':keydata_channel,'keydata_os':keydata_os,'keydata_device':keydata_device,'image':image})
    else:
        return render(request,"dashboard.html",{})



def suggestions(request):
    subscription = request.session['subscription']
    if subscription == 'Standard' or subscription == 'Premium':
        clientID = request.session['clientID']
        report_data = list(Report.objects.filter(clientID = clientID ))
        if len(report_data)>0:
            report_data_current=report_data[-1]
            f_id = list(TopFeature.objects.filter(reportID = report_data_current.ID).values_list('featureID',flat=True))
            my_list = list()
            my_list1 = list()
            #print(all_month)
            for i,f in enumerate(f_id):
                f_type=list(FeatureType.objects.filter(id = f))
                #new_lst=(','.join(str(a)for a in f_type))
                my_list.append(f_type)
                suggestion=  list(FeatureSuggestion.objects.filter(featureID = f))
                my_list1.append(suggestion)        
            # print(report_data_current)
            return render(request,"suggestions.html",{'f_type':my_list,'s_name':my_list1})

        else:
            return render(request,"suggestions.html",{})
        
    

def customers(request):
    clientID = request.session['clientID']
    report_id = list(Report.objects.filter(clientID = clientID ).values_list('ID',flat=True))
    if len(report_id)>0:
        keydata_city = list(KeyData.objects.filter(keyDataTypeID = 1 , reportID = report_id[-1] ))
        keydata_sum = KeyData.objects.aggregate(total =Sum('revenue',filter=Q(keyDataTypeID = 1 , reportID = report_id[-1] )))
        userCount_sum = KeyData.objects.aggregate(total =Sum('userCount',filter=Q(keyDataTypeID = 1 , reportID = report_id[-1] )))
        conversionRate_sum = KeyData.objects.aggregate(total =Sum('conversionRate',filter=Q(keyDataTypeID = 1 , reportID = report_id[-1] )))

        customer_segmantaion_data = SegmentationData.objects.get(segmentType = 'RFMX' , reportID = report_id[-1] ) if SegmentationData.objects.filter(segmentType = 'RFMX' , reportID = report_id[-1] ).exists() else True
        #new_lst=(','.join(str(a)for a in keydata_city))
        print(customer_segmantaion_data)
        return render(request,"customers.html",{'keydata_city':keydata_city,'sum':keydata_sum['total'],'sum1':userCount_sum['total'],'sum2':conversionRate_sum['total'],'customer_segmantaion_data':customer_segmantaion_data})
    else:
        return render(request,"customers.html",{})

def visitors(request):
    clientID = request.session['clientID']
    report_id = list(Report.objects.filter(clientID = clientID ).values_list('ID',flat=True))
    if len(report_id)>0:
        visitor_segmantaion_data = SegmentationData.objects.get(segmentType = 'KNNX' , reportID = report_id[-1] )if SegmentationData.objects.filter(segmentType = 'KNNX' , reportID = report_id[-1]).exists() else True
        v_seg_top_dxi  = list(VisitorSegmentation.objects.values().filter(userRank = 1 , reportID =  report_id[-1], metaInfo = 'Top DXI'))
        v_seg_low_dxi  = list(VisitorSegmentation.objects.values().filter(userRank = 1 , reportID =  report_id[-1], metaInfo = 'Bottom DXI'))
        v_seg_top_buyer  = list(VisitorSegmentation.objects.values().filter(userRank = 1 , reportID =  report_id[-1], metaInfo = 'Top Buyers')) 
        print(v_seg_top_dxi)
        #query for topdxi
        seg_list_top_dxi = []
        featureName_list = []
        content2 = {}
        for i,v in enumerate(v_seg_top_dxi):
            fid= v_seg_top_dxi[i]['featureID_id']
            seg_list_top_dxi.append(fid)
        for i,f in enumerate(seg_list_top_dxi):
            f_name= (FeatureType.objects.get(id = f))
            content2 = {'obj': f_name}
            featureName_list.append(content2)

        #query for lowdxi
        seg_list_low_dxi = []
        featureName_list2 = []
        content2 = {}
        for i,v in enumerate(v_seg_low_dxi):
            fid1= v_seg_low_dxi[i]['featureID_id']
            seg_list_low_dxi.append(fid1)
        for i,f in enumerate(seg_list_low_dxi):
            f_name2= (FeatureType.objects.get(id = f))
            content3 = {'obj': f_name2}
            featureName_list2.append(content3)

        #query for Top Buyers list
        seg_list_top_buyer = []
        featureName_list3 = []
        content2 = {}
        for i,v in enumerate(v_seg_top_buyer):
            fid2= v_seg_top_buyer[i]['featureID_id']
            seg_list_top_buyer.append(fid2)
        for i,f in enumerate(seg_list_top_buyer):
            f_name3= (FeatureType.objects.get(id = f))
            content4 = {'obj': f_name3}
            featureName_list3.append(content4)

        return render(request,"visitors.html",{'visitor_segmantaion_data':visitor_segmantaion_data,'v_seg_top_dxi':v_seg_top_dxi,'featureName_list':featureName_list,'v_seg_low_dxi':v_seg_low_dxi,'featureName_list2':featureName_list2,'v_seg_top_buyer':v_seg_top_buyer,'featureName_list3':featureName_list3})
    else:
        msg = 'Data Not Found'
        return render(request,"nodata.html",{'msg':msg})

def glossary(request):
    return render(request,"glossary.html",{})
    
def si_report(request):
    if request.method == 'GET':
        r_id = request.GET['r_month']
        s_data = Report.objects.values().filter(ID=r_id)
        s2_data = SummaryInsights.objects.values().filter(reportID=r_id)
        summary_data = list(s2_data)
        clientID = request.session['clientID']
        #r_data = Report.objects.values().filter(clientID = clientID )
        #report_data=list(r_data)
        f_id = list(TopFeature.objects.filter(reportID = r_id).values_list('featureID',flat=True))
        
      # my_list.append(f_type)
        print("print fid")
        #print(f_id)
        suggestion_list = []
        content6 = {}
        f_list1 =  []
        s_list1 =  []
        for i,f in enumerate(f_id):
            print(f)
            f_type=FeatureType.objects.values().get(id = f)
            f_list1.append(f_type)
            f_list=list(f_list1)
            
            
            suggestion= list(FeatureSuggestion.objects.values().filter(featureID = f))
            s_list1.append(suggestion)

            content6 = {'type': f_type,'list':suggestion}
            suggestion_list.append(content6)

            feature_suggestion_list=list(s_list1)
        print('**********************  suggestion_list ********************************')
        print(suggestion_list)    
        p_data = list(s_data)
        keydata_city = KeyData.objects.values().filter(keyDataTypeID = 1 , reportID = r_id )
        city = list(keydata_city)
        customer_segmantaion_data_1 = SegmentationData.objects.values().get(segmentType = 'RFMX' , reportID  = r_id )if SegmentationData.objects.filter(segmentType = 'RFMX' , reportID = r_id ).exists() else True
        keydata_sum = KeyData.objects.aggregate(total =Sum('revenue',filter=Q(keyDataTypeID = 1 , reportID = r_id )))
        userCount_sum = KeyData.objects.aggregate(total =Sum('userCount',filter=Q(keyDataTypeID = 1 , reportID = r_id )))
        conversionRate_sum = KeyData.objects.aggregate(total =Sum('conversionRate',filter=Q(keyDataTypeID = 1 , reportID = r_id )))
        visitor_segmantaion_data_1= SegmentationData.objects.values().get(segmentType = 'KNNX' , reportID  = r_id )if SegmentationData.objects.filter(segmentType = 'KNNX' , reportID = r_id ).exists() else True
        transaction_summary = TransactionSummary.objects.values().get( reportID = r_id )if TransactionSummary.objects.filter( reportID = r_id ).exists() else True
        product_list = list(Product.objects.values().filter(clientID = clientID ))
        topproduct_list = list(TopProduct.objects.values().filter( reportID = r_id ))
        similar_product_list = list(CNNSimilarProduct.objects.values().filter( reportID = r_id ))
        market_basket_top = list(MarketBasket.objects.values().filter( sortingOrder = 'Top', reportID = r_id))
        market_basket_bottom = list(MarketBasket.objects.values().filter( sortingOrder = 'Bottom', reportID = r_id))
        keydata_browser = list(ClusterData.objects.values().filter(keyDataTypeID = 2 , reportID = r_id ))
        keydata_city = list(ClusterData.objects.values().filter(keyDataTypeID = 1 , reportID = r_id ))
        keydata_os = list(ClusterData.objects.values().filter(keyDataTypeID = 3 , reportID = r_id ))
        keydata_device = list(ClusterData.objects.values().filter(keyDataTypeID = 5 , reportID = r_id ))
        keydata_channel = list(ClusterData.objects.values().filter(keyDataTypeID = 4 , reportID = r_id ))
        keydata_social = list(ClusterData.objects.values().filter(keyDataTypeID = 6 , reportID = r_id ))
        keydata_channel_overview = list(KeyData.objects.values().filter(keyDataTypeID = 4 , reportID = r_id ))
        keydata_browser_overview = list(KeyData.objects.values().filter(keyDataTypeID = 2 , reportID = r_id ))
        keydata_os_overview = list(KeyData.objects.values().filter(keyDataTypeID = 3 , reportID = r_id ))
        keydata_device_overview = list(KeyData.objects.values().filter(keyDataTypeID = 5 , reportID = r_id))
        v_seg_top_dxi  = list(VisitorSegmentation.objects.values().filter(userRank = 1 , metaInfo = 'Top DXI', reportID =  r_id))
        v_seg_low_dxi  = list(VisitorSegmentation.objects.values().filter(userRank = 1 , reportID =  r_id , metaInfo = 'Bottom DXI'))
        v_seg_top_buyer  = list(VisitorSegmentation.objects.values().filter(userRank = 1 , reportID =  r_id, metaInfo = 'Top Buyers')) 
        print("VINOD_____________________________________________________________________")
        print(v_seg_top_dxi)
        #query for topdxi
        seg_list_top_dxi = []
        featureName_list = []
        content2 = {}
        for i,v in enumerate(v_seg_top_dxi):
            fid= v_seg_top_dxi[i]['featureID_id']
            seg_list_top_dxi.append(fid)
        for i,f in enumerate(seg_list_top_dxi):
            f_name= list(FeatureType.objects.values().filter(id = f))
            content2 = {'obj': f_name}
            featureName_list.append(content2)

        #query for lowdxi
        seg_list_low_dxi = []
        featureName_list2 = []
        content2 = {}
        for i,v in enumerate(v_seg_low_dxi):
            fid1= v_seg_low_dxi[i]['featureID_id']
            seg_list_low_dxi.append(fid1)
        for i,f in enumerate(seg_list_low_dxi):
            f_name2=list(FeatureType.objects.values().filter(id = f))
            content3 = {'obj': f_name2}
            featureName_list2.append(content3)

        #query for Top Buyers list
        seg_list_top_buyer = []
        featureName_list3 = []
        content2 = {}
        for i,v in enumerate(v_seg_top_buyer):
            fid2= v_seg_top_buyer[i]['featureID_id']
            seg_list_top_buyer.append(fid2)
        for i,f in enumerate(seg_list_top_buyer):
            f_name3=list(FeatureType.objects.values().filter(id = f))
            content4 = {'obj': f_name3}
            featureName_list3.append(content4)

        histogram_img = Collateral.objects.values().get(reportID = r_id , typeName = 'Composite DXI histogram' )if Collateral.objects.filter(reportID = r_id, typeName = 'Composite DXI histogram').exists() else True
        if histogram_img != True:
         image_histo = b64encode(histogram_img['collateralContent']).decode("utf-8")
         return JsonResponse({"k_city":city, "period":p_data, "summary":summary_data,"customer_segmantaion_data_1":customer_segmantaion_data_1,"visitor_segmantaion_data_1":visitor_segmantaion_data_1,"top_feature_list":f_list,"feature_suggestion_list":feature_suggestion_list,"rev_sum":keydata_sum['total'],"usercount_sum":userCount_sum['total'],"con_rate_sum":conversionRate_sum['total'],"t_summary":transaction_summary,"market_basket_top":market_basket_top,"market_basket_bottom":market_basket_bottom,"product_list":product_list,"topproduct_list":topproduct_list,"similar_product_list":similar_product_list,"keydata_browser":keydata_browser,"keydata_city":keydata_city,"keydata_os":keydata_os,"keydata_device":keydata_device,"keydata_channel":keydata_channel,"keydata_social":keydata_social,'keydata_channel_overview':keydata_channel_overview,'keydata_os_overview':keydata_os_overview,'keydata_browser_overview':keydata_browser_overview,'keydata_device_overview':keydata_device_overview,'featureName_list':featureName_list,'v_seg_top_dxi':v_seg_top_dxi,'v_seg_low_dxi':v_seg_low_dxi,'featureName_list2':featureName_list2,'v_seg_top_buyer':v_seg_top_buyer,'featureName_list3':featureName_list3,'image_histo':image_histo,'suggestion_list':suggestion_list})
        else:
            msg = 'No Data Found'
 
        return JsonResponse({"k_city":city, "period":p_data, "summary":summary_data,"customer_segmantaion_data_1":customer_segmantaion_data_1,"visitor_segmantaion_data_1":visitor_segmantaion_data_1,"top_feature_list":f_list,"feature_suggestion_list":feature_suggestion_list,"rev_sum":keydata_sum['total'],"usercount_sum":userCount_sum['total'],"con_rate_sum":conversionRate_sum['total'],"t_summary":transaction_summary,"market_basket_top":market_basket_top,"market_basket_bottom":market_basket_bottom,"product_list":product_list,"topproduct_list":topproduct_list,"similar_product_list":similar_product_list,"keydata_browser":keydata_browser,"keydata_city":keydata_city,"keydata_os":keydata_os,"keydata_device":keydata_device,"keydata_channel":keydata_channel,"keydata_social":keydata_social,'keydata_channel_overview':keydata_channel_overview,'keydata_browser_overview':keydata_browser_overview,'keydata_os_overview':keydata_os_overview,'featureName_list':featureName_list,'v_seg_top_dxi':v_seg_top_dxi,'v_seg_low_dxi':v_seg_low_dxi,'featureName_list2':featureName_list2,'v_seg_top_buyer':v_seg_top_buyer,'featureName_list3':featureName_list3,'msg':msg,'suggestion_list':suggestion_list})

        
        
        