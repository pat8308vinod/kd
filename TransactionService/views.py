from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from accounts.models import UserProfile
from django.http.response import JsonResponse,json
from KeydabraManagerController.models import Report
from TransactionService.models import TransactionSummary, TopProduct, CNNRecommender,Product,MarketBasket,CNNSimilarProduct
from TransactionService.serializers import TransactionSummarySerializer, TopProductSerializer, CNNRecommenderSerializer


# Create your views here.
@api_view(['POST'])
def getTransactionSummary(request):
    if request.method == 'POST':
        summary_data = JSONParser().parse(request)
        summary = TransactionSummary.objects.get(reportID = summary_data['reportID'])
        transactional = {
            'income': summary.income,
            'transactions': summary.transactions,
            'itemsInPurchase': summary.itemsInPurchase,
            'avgSizeOfPurchase': summary.avgSizeOfPurchase
        }
        return Response(transactional)


@api_view(['POST'])
def getTopProducts(request):
    if request.method == 'POST':
        summary_data = JSONParser().parse(request)
        summary = TopProduct.objects.get(reportID = summary_data['reportID'])
        transactional = {
            'income': summary.income,
            'transactions': summary.transactions,
            'itemsInPurchase': summary.itemsInPurchase,
            'avgSizeOfPurchase': summary.avgSizeOfPurchase
        }
        return Response(transactional)


@api_view(['POST'])
def addTopProduct(request):
    if request.method == 'POST':
        summary_data = JSONParser().parse(request)
        summary_serializer = TopProductSerializer(data=summary_data)
        if summary_serializer.is_valid():
            summary_serializer.save()
            return Response(summary_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(summary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addTransactionSummary(request):
    if request.method == 'POST':
        summary_data = JSONParser().parse(request)
        summary_serializer = TransactionSummarySerializer(data=summary_data)
        if summary_serializer.is_valid():
            summary_serializer.save()
            return Response(summary_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(summary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addCNNRecommendations(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        recomm_serializer = CNNRecommenderSerializer(data=request_data)
        if recomm_serializer.is_valid():
            recomm_serializer.save()
            return Response(recomm_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(recomm_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def transactions(request):
    clientID = request.session['clientID']
    report_id = list(Report.objects.filter(clientID = clientID ).values_list('ID',flat=True))
    if len(report_id)>0:
        transaction_summary = TransactionSummary.objects.get( reportID = report_id[-1] )if TransactionSummary.objects.filter( reportID = report_id[-1] ).exists() else True
        transaction_summary_1 = TransactionSummary.objects.get( reportID = report_id[-2] )if TransactionSummary.objects.filter( reportID = report_id[-2] ).exists() else True
        report_data = list(Report.objects.filter(clientID = clientID ))
        current_month=report_data[-1]
        previous_month=report_data[-2]
        topproduct_list = list(TopProduct.objects.filter( reportID = report_id[-1] ).values_list('productID','quantity'))
        product_list = list(Product.objects.filter(clientID = clientID ))
        similar_product_list = list(CNNSimilarProduct.objects.filter( reportID = report_id[-1] ))

        market_basket_top = list(MarketBasket.objects.filter( sortingOrder = 'Top',reportID = report_id[-1]))
        market_basket_bottom = list(MarketBasket.objects.filter( sortingOrder = 'Bottom',reportID = report_id[-1]))
        print("***********similar_product_list*************")
        print(similar_product_list)
        product_lst_top = []
        content = {}
        for result in topproduct_list:
            content = {'id': result[0], 'quntity': result[1]}
            product_lst_top.append(content)
        print(product_lst_top)

        print("TPO PRODUCT---------------------------------")
        print(product_list)
        return render(request,"transactions.html",{'transaction_summary':transaction_summary,'transaction_summary_1':transaction_summary_1,'current_month':current_month,'previous_month':previous_month,'product_list':product_list,'product_lst_top':product_lst_top,'market_basket_top':market_basket_top,'market_basket_bottom':market_basket_bottom,'similar_product_list':similar_product_list})
    else:
        return render(request,"transactions.html",{})    