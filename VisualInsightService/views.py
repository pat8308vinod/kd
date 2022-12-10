from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from VisualInsightService.serializers import ClientSitePageSerializer, HeatMapSerializer, TopFeatureSerializer
from VisualInsightService.serializers import CustomerFlowSerializer, FlowPageOrderSerializer

# Create your views here.
@api_view(['POST'])
def addClientSitePage(request):
    if request.method == 'POST':
        sitepage_data = JSONParser().parse(request)
        sitepage_ser = ClientSitePageSerializer(data=sitepage_data)
        if sitepage_ser.is_valid():
            sitepage_ser.save()
            return Response(sitepage_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sitepage_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addHeatMap(request):
    if request.method == 'POST':
        heatmap_data = JSONParser().parse(request)
        heatmap_ser = HeatMapSerializer(data=heatmap_data)
        if heatmap_ser.is_valid():
            heatmap_ser.save()
            return Response(heatmap_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(heatmap_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addCustomerFlow(request):
    if request.method == 'POST':
        custflow_data = JSONParser().parse(request)
        custflow_ser = CustomerFlowSerializer(data=custflow_data)
        if custflow_ser.is_valid():
            custflow_ser.save()
            return Response(custflow_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(custflow_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addFlowPageOrder(request):
    if request.method == 'POST':
        floworder_data = JSONParser().parse(request)
        floworder_ser = FlowPageOrderSerializer(data=floworder_data)
        if floworder_ser.is_valid():
            floworder_ser.save()
            return Response(floworder_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(floworder_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addTopFeature(request):
    if request.method == 'POST':
        topfeature_data = JSONParser().parse(request)
        topfeature_ser = TopFeatureSerializer(data=topfeature_data)
        if topfeature_ser.is_valid():
            topfeature_ser.save()
            return Response(topfeature_ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(topfeature_ser.errors, status=status.HTTP_400_BAD_REQUEST)