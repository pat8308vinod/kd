import base64
import datetime as dt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from ClientManagementService.models import Client
from KeydabraManagerController.models import Report
from SummaryDXIInsightService.models import SummaryInsights, Statements, Collateral
from KeyDataService.models import KeyDataType, KeyData, Location, SegmentationData
from TransactionService.models import TransactionSummary, Product, TopProduct
from TransactionService.models import CNNRecommender, CNNSimilarProduct, MarketBasket
from VisualInsightService.models import ClientSitePage, FeatureType, HeatMap
from VisualInsightService.models import CustomerFlow, FlowPageOrder, TopFeature, FeatureSuggestion
from VisualInsightService.models import VisitorSegmentation
from BehavioralInsightService.models import WordCloud, ReviewSentiment, ClusterData
from PrescriptionService.models import Prescription
from ClientReportController import utils


# Create your views here.
def getKeyWebData(report_id):
    keyData = KeyData.objects.filter(reportID=report_id)
    print('report_id is: ', report_id, ', keyData length is: ', len(keyData))
    cities = set()
    cityDetails, browserDetails, channelDetails, deviceDetails, osDetails = ([] for _ in range(5))
    for keyDetail in keyData:
        keyDatail_dict = dict()
        keyDatail_dict['userCount'] = keyDetail.userCount
        keyDatail_dict['revenue'] = keyDetail.revenue
        keyDatail_dict['conversionRate'] = keyDetail.conversionRate
        keyDatail_dict['name'] = keyDetail.name
            
        keydatatype_id = keyDetail.keyDataTypeID.ID
        if keydatatype_id == 1:
            cityDetails.append(keyDatail_dict)
            cities.add(keyDatail_dict['name'])
        elif keydatatype_id == 2:
            browserDetails.append(keyDatail_dict)
        elif keydatatype_id == 3:
            osDetails.append(keyDatail_dict)
        elif keydatatype_id == 4:
            channelDetails.append(keyDatail_dict)
        elif keydatatype_id == 5:
            deviceDetails.append(keyDatail_dict)
    
    if len(cityDetails) > 0:
        locations = Location.objects.filter(city__in=cities)
        cityloc_dict = {}
        for loc in locations:
            cityloc_dict[loc.city] = {
                'state': loc.state,
                'country': loc.country,
                'countryCode': loc.countryCode
            }
        for detail in cityDetails:
            city = detail['name']
            try:
                detail['state'] = cityloc_dict[city]['state']
                detail['country'] = cityloc_dict[city]['country']
                detail['countryCode'] = cityloc_dict[city]['countryCode']
            except KeyError:
                detail['state'] = None
                detail['country'] = None
                detail['countryCode'] = None
    
    key_data = {
        'city_data': cityDetails,
        'browser_data': browserDetails,
        'channel_data': channelDetails,
        'device_data': deviceDetails,
        'os_data': osDetails
    }
    return key_data

def getCollateralData(collaterals):
    collateral_data = dict()
    for collateral in collaterals:
        print('collateral.id:', collateral.id)
        base64_data = base64.b64encode(collateral.collateralContent).decode("utf-8")
        collateral_data[collateral.id] = {
            'contentType': collateral.collateralMimeType,
            'content': base64_data
        }
    return collateral_data

def getObservationData(predictions, collaterals=None):
    if collaterals is not None:
        collateral_data = dict()
        for collateral in collaterals:
            base64_data = base64.b64encode(collateral.collateralContent).decode("utf-8")
            collateral_data[collateral.typeID] = {
                'statementType': collateral.typeName,
                'statementID': collateral.typeID,
                'contentType': collateral.collateralMimeType,
                'content': base64_data
            }

    prediction_data = []
    for prediction in predictions:
        prediction_dict = dict()
        statement_id = prediction.ID
        prediction_dict['statementID'] = statement_id
        prediction_dict['statementText'] = prediction.statementText
        if prediction.solutionText is not None:
            prediction_dict['solutionText'] = prediction.solutionText
        # setting reference image to the recommendation
        prediction_dict['informationType'] = prediction.informationType
        if (collaterals is not None) and (statement_id in collateral_data):
            prediction_dict['collateral'] = collateral_data[statement_id]
        prediction_data.append(prediction_dict)
    return prediction_data

@api_view(['POST'])
def getDashboardSummary(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])
        report_details = {
            'id': report_data.pk,
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod
        }
        print(report_details)

        ### Timeseries        
        reports = Report.objects.filter(clientID_id=client_data.ID).order_by('-toPeriod')
        report_ids, insight_ids = [list() for _ in range(2)]
        months_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
        'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
        'November': 11, 'December': 12}
        for report in reports:
            if (report.toPeriod <= report_data.toPeriod) and (len(report_ids) < 5):
                report_ids.append(report.pk)

        print('report_ids:', reports)
        summary_insights = SummaryInsights.objects.filter(reportID__in=report_ids).order_by('-ID')
        summary_dict = dict()
        # sort by month
        sortedSummaryInsights = utils.sortByMonth(report_ids, summary_insights)
        for summary in sortedSummaryInsights:
            insight_ids.append(summary.ID)
            summary_dict[summary.month] = {
                'DXI': utils.getFloatVal(summary.DXI),
                'TargetDXI': utils.getFloatVal(summary.TargetDXI),
                'currentConversionRate': utils.getFloatVal(summary.currentConversionRate),
                'targetConversionRate': utils.getFloatVal(summary.targetConversionRate),
                'visitors': summary.visitors,
                'uniqueBuyers': summary.uniqueBuyers,
                'prospectiveBuyers': summary.prospectiveBuyers,
                'netDollarValue': utils.getFloatVal(summary.netDollarValue),
                'topDXIConversionRate': utils.getFloatVal(summary.topDXIConversionRate),
                'lowDXIConversionRate': utils.getFloatVal(summary.lowDXIConversionRate),
                'behavioralDXI': utils.getFloatVal(summary.BehavioralDXI),
                'KPIDXI': utils.getFloatVal(summary.KPIDXI),
                'transactionalDXI': utils.getFloatVal(summary.TransactionalDXI),
                'visualDXI': utils.getFloatVal(summary.VisualDXI),
                'bestSource': summary.bestSource,
                'bestSeller': summary.bestSeller,
                'allAppDownloads': summary.allAppDownloads
            }
        first_two_insights = list(summary_dict.keys())[:2]
        print('len(first_two_insights):', len(first_two_insights), ':', first_two_insights)
        if len(first_two_insights) > 1:
            summary_dict['netDollarValueIncreased'] = utils.compareValues(
                utils.getFloatVal(summary_dict[first_two_insights[0]]['netDollarValue']), 
                utils.getFloatVal(summary_dict[first_two_insights[1]]['netDollarValue'])
            )
            summary_dict['uniqueBuyersIncreased'] = utils.compareValues(
                utils.getFloatVal(summary_dict[first_two_insights[0]]['uniqueBuyers']), 
                utils.getFloatVal(summary_dict[first_two_insights[1]]['uniqueBuyers'])
            )
            summary_dict['visitorsIncreased'] = utils.compareValues(
                utils.getFloatVal(summary_dict[first_two_insights[0]]['visitors']), 
                utils.getFloatVal(summary_dict[first_two_insights[1]]['visitors'])
            )
            summary_dict['currentConversionRateIncreased'] = utils.compareValues(
                utils.getFloatVal(summary_dict[first_two_insights[0]]['currentConversionRate']), 
                utils.getFloatVal(summary_dict[first_two_insights[1]]['currentConversionRate'])
            )
            summary_dict['targetDXIIncreased'] = utils.compareValues(
                utils.getFloatVal(summary_dict[first_two_insights[0]]['TargetDXI']), 
                utils.getFloatVal(summary_dict[first_two_insights[1]]['TargetDXI'])
            )
            summary_dict['targetConversionRateIncreased'] = utils.compareValues(
                utils.getFloatVal(summary_dict[first_two_insights[0]]['targetConversionRate']), 
                utils.getFloatVal(summary_dict[first_two_insights[1]]['targetConversionRate'])
            )
        else:
            summary_dict['netDollarValueIncreased'] = None
            summary_dict['uniqueBuyersIncreased'] = None
            summary_dict['visitorsIncreased'] = None
            summary_dict['currentConversionRateIncreased'] = None
            summary_dict['targetDXIIncreased'] = None
            summary_dict['targetConversionRateIncreased'] = None
    
        predictions = Statements.objects.filter(
            reportID = report_data.pk, statementType='PRED', overviewFlag=True
        )

        prediction_data = getObservationData(predictions)
        
        inferences = Statements.objects.filter(
            reportID = report_data.pk, statementType='INFER', statementSubtype='DXI'
        )
        inference_data = dict()
        for inference in inferences:
            inference_data[inference.ID] = inference.statementText
        
        insights = Statements.objects.filter(
            reportID = report_data.pk, statementType='INSIGHT', statementSubtype='DXI', 
            informationType='Overview'
        )
        insight_data = dict()
        for insight in insights:
            insight_data[insight.ID] = insight.statementText
        
        source_data = getKeyWebData(report_data.pk)

        collaterals = Collateral.objects.filter(
            reportID=report_data.pk, typeName='Composite DXI histogram'
        )
        composite_histogram = getCollateralData(collaterals)
        response_data = {
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod,
            'reportID': report_data.pk,
            'summaryInsights': summary_dict,
            'predictions': prediction_data,
            'inferences': inference_data,
            'insights': insight_data,
            'source': source_data,
            'histogram': composite_histogram,
            'subscription': client_data.subscription
        }
        return Response(response_data)


@api_view(['POST'])
def getPredictionsAndPrescriptions(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id = client_data.ID, forMonth=req_data['forMonth'])

        collaterals = Collateral.objects.filter(reportID=report_data.pk)
        predictions = Statements.objects.filter(reportID=report_data.pk, statementType='PRED')        
        prediction_data = getObservationData(predictions, collaterals)
        
        insights = Statements.objects.filter(
            reportID=report_data.pk, statementType='INSIGHT', informationType='Recommendations'
        )
        insight_data = dict()
        for insight in insights:
            insight_data[insight.ID] = insight.statementText
        
        prescriptions = Prescription.objects.filter(implementationStatus=False)
        prescription_data = []
        for prescription in prescriptions:
            prescription_data.append({
                'id': prescription.ID, 'report': prescription.reportForMonth,
                'section': prescription.prescriptionSection,
                'strategy': prescription.prescriptionName if prescription.prescriptionText is None else prescription.prescriptionText,
                'implement_date': None if prescription.implementaionDate is None else prescription.implementaionDate,
                'implement_status': prescription.implementationStatus
            })
        print('No of presc retrieved:', len(prescriptions), ', len in response:', len(prescription_data))
        
        response_data = {
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod,
            'reportID': report_data.pk,
            'predictions': prediction_data,
            'insights': insight_data,
            'prescriptions': prescription_data,
            'subscription': client_data.subscription
        }
        return Response(response_data)


@api_view(['POST'])
def getKeyData(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])
        
        summary = SummaryInsights.objects.get(reportID=report_data.pk)        
        source_data = getKeyWebData(report_data.pk)

        insights = Statements.objects.filter(
            reportID=report_data.pk, statementType='INSIGHT', informationType='Customers'
        )
        insight_data = dict()
        for insight in insights:
            insight_data[insight.ID] = insight.statementText
        
        collaterals = Collateral.objects.filter(reportID=report_data.pk)

        predictions = Statements.objects.filter(
            reportID=report_data.pk, statementType='PRED', informationType='Customers'
        )
        prediction_data = getObservationData(predictions, collaterals)

        segmentation_dict = dict()
        segmentations = SegmentationData.objects.filter(reportID=report_data.pk)
        for segment in segmentations:
            segmentation_dict[segment.segmentType] = {
                'loosing': segment.loosingScore,
                'loyal': segment.loyalScore,
                'hibernating': segment.hibernatingScore,
                'top': segment.topScore
            }
        
        response_data = {
            'companyName': client_data.companyName,
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod,
            'reportID': report_data.pk,
            'revenue': summary.netDollarValue,
            'visits': summary.visitors,
            'conversionRate': summary.currentConversionRate,
            'DXI': summary.DXI,
            'insights': insight_data,
            'source': source_data,
            'observations': prediction_data,
            'segmentation': segmentation_dict,
            'subscription': client_data.subscription
        }        
    return Response(response_data)

def getReportMonth(reports, report_id):
    for report in reports:
        if report.pk == report_id:
            return report.forMonth

@api_view(['POST'])
def getTransactionalInsights(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        # client_data = Client.objects.get(companyName=req_data['companyName'])
        # report_data = Report.objects.get(clientID_id = client_data.ID, forMonth=req_data['forMonth'])
        client_data, report_data = utils.getReportData(req_data['companyName'], req_data['forMonth'])
        reports = Report.objects.filter(clientID_id=client_data.ID).order_by('-toPeriod')[:2]
        report_ids, collateral_ids, source_ids = [list() for _ in range(3)]
        for report in reports:
            if (report.toPeriod <= report_data.toPeriod) and (len(report_ids) < 5):
                report_ids.append(report.pk)

        # transactions = TransactionSummary.objects.filter(reportID__in=[reports[0].pk, reports[1].pk])
        transactions = TransactionSummary.objects.filter(reportID__in=report_ids)
        transaction_data = dict()
        for transaction in transactions:
            month = getReportMonth(reports, transaction.reportID.ID)
            transaction_data[month] = {
                'income': transaction.income,
                'transactions': transaction.transactions,
                'itemsInPurchase': transaction.itemsInPurchase,
                'avgSizeOfPurchase': transaction.avgSizeOfPurchase
            }

        topProducts = TopProduct.objects.filter(reportID=reports[0].pk)
        products = Product.objects.filter(clientID=client_data.ID)
        top_products_data, prod_collat_dict, cnn_prod_dict, collat_dict, top_similar_dict = (dict() for _ in range(5))
        for prod in products:
            # productname_dict[prod.ID] = prod.productName
            if prod.collateralID is not None:
                prodCollat_id = prod.collateralID.id
            else:
                prodCollat_id = None
            prod_collat_dict[prod.ID] = {
                'prodName': prod.productName,
                'prodDesc': prod.productDesc,
                'prodCollat': prodCollat_id
            }
            if prodCollat_id:
                collateral_ids.append(prod.collateralID.id)

        insights = Statements.objects.filter(
            reportID=report_data.pk, statementType='INSIGHT', informationType='Transactions'
        )
        insight_data = dict()
        for insight in insights:
            insight_data[insight.ID] = insight.statementText
        
        collaterals = Collateral.objects.filter(reportID=report_data.pk)
        predictions = Statements.objects.filter(
            reportID=report_data.pk, statementType='PRED', informationType='Transactions'
        )
        prediction_data = getObservationData(predictions, collaterals)

        # cnn
        recommenders = CNNRecommender.objects.filter(reportID=report_data.pk)
        for recom in recommenders:
            source_ids.append(recom.productID.ID)
        similarprods = CNNSimilarProduct.objects.filter(sourceProdID_id__in=source_ids)
        
        collaterals = Collateral.objects.filter(id__in=collateral_ids)
        for img in collaterals:
            base64_data = base64.b64encode(img.collateralContent).decode("utf-8")
            collat_dict[img.id] = {
                'mimeType': img.collateralMimeType,
                'content': base64_data
            }
        cnn_similar_dict = dict()
        for similarprod in similarprods:
            source_id = similarprod.sourceProdID_id
            recomm_id = similarprod.recommendedProdID_id
            recomm_prod_name = prod_collat_dict[recomm_id]['prodName']
            recomm_similarity_score = utils.getFloatVal(similarprod.similarityScore)
            recomm_collat_id = prod_collat_dict[source_id]['prodCollat'] if prod_collat_dict[source_id] is not None else None
            recomm_collat_data = collat_dict[recomm_collat_id] if recomm_collat_id is not None else None
            similar_dict = {
                'recomm_id': recomm_id,
                'recomm_prod_name': recomm_prod_name,
                'recomm_similarity_score': recomm_similarity_score,
                'recomm_collat_data': recomm_collat_data
            }
            if source_id not in cnn_similar_dict:
                cnn_similar_dict[source_id] = list()
                cnn_similar_dict[source_id].append(similar_dict)
            else:
                cnn_similar_dict[source_id].append(similar_dict)
        for source_id in source_ids:
            src_prod_name = prod_collat_dict[source_id]['prodName']
            src_prod_collat_id = prod_collat_dict[source_id]['prodCollat'] if prod_collat_dict[source_id] is not None else None
            src_collat_data = collat_dict[src_prod_collat_id] if src_prod_collat_id is not None else None
            cnn_prod_dict[source_id] = {
                'source_id': source_id,
                'src_prod_name': src_prod_name,
                'src_collat_data': src_collat_data if src_collat_data is not None else None,
                'cnn_recomm_prods': cnn_similar_dict[source_id]
            }
        top_prod_ids = [prod.productID.ID for prod in topProducts]
        similar_top_prods = CNNSimilarProduct.objects.filter(
            reportID=report_data.pk, sourceProdID_id__in=top_prod_ids
        )
        for prod in similar_top_prods:
            top_prod_id = prod.sourceProdID_id
            similar_prod_id = prod.recommendedProdID_id
            similar_prod_name = prod_collat_dict[similar_prod_id]['prodName']
            if top_prod_id not in top_similar_dict:
                top_similar_dict[top_prod_id] = list()
                top_similar_dict[top_prod_id].append(similar_prod_name)
            else:
                top_similar_dict[top_prod_id].append(similar_prod_name)
        for top_product in topProducts:
            product_name = prod_collat_dict[top_product.productID.ID]['prodName']
            product_id = top_product.productID.ID
            similar_prods = top_similar_dict[product_id] if product_id in top_similar_dict else None
            top_products_data[product_id] = {
                'prod_id': product_id,
                'product_name': product_name,
                'quantity': top_product.quantity,
                'similar_products': similar_prods
            }
        print('Top products source ids:', top_products_data.keys())
        print('CNN products source ids:', cnn_prod_dict.keys())

        # market basket
        marketBasket_data = dict()
        marketBasket = MarketBasket.objects.filter(reportID=report_data.pk)
        for combination in marketBasket:
            antecedent_id = combination.antecedentProdID.ID
            consequent_id = combination.consequentProdID.ID
            sorting_order = combination.sortingOrder
            combination_dict = {
                'antecedent_name': prod_collat_dict[antecedent_id]['prodName'],
                # 'antecedent_collat':  prod_collat_dict[antecedent_id]['prodCollat'] if prod_collat_dict[antecedent_id] is not None else None,
                'consequent_name': prod_collat_dict[consequent_id]['prodName'],
                # 'consequent_collat': prod_collat_dict[consequent_id]['prodCollat'] if prod_collat_dict[consequent_id] is not None else None,
                'confidence_score': combination.confidenceScore,
                'lift_score': combination.liftScore,
                'combination_rank': combination.combinationRank
            }
            if sorting_order not in marketBasket_data:
                marketBasket_data[sorting_order] = list()
                marketBasket_data[sorting_order].append(combination_dict)
            else:
                marketBasket_data[sorting_order].append(combination_dict)

        response_data = {
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod,
            'reportID': report_data.pk,
            'transactional': transaction_data,
            'topProducts': top_products_data,
            'insights': insight_data,
            'observations': prediction_data,
            'cnn_data': cnn_prod_dict,
            'marketbasket': marketBasket_data,
            'subscription': client_data.subscription
        }
        return Response(response_data)

@api_view(['POST'])
def getVisualInsights(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])

        observations = Statements.objects.filter(
            reportID = report_data.pk, statementType='HEATMAP', informationType='Site'
        )
        observation_dict = dict()
        for observation in observations:
            statement_id = observation.ID
            observation_dict[statement_id] = {
                'statementText': observation.statementText,
                'solutionText': observation.solutionText #if prediction.solutionText is not None
            }
            
        collaterals = Collateral.objects.filter(reportID = report_data.pk, typeName='HEATMAP')
        collateral_data = dict()
        collateral_ids = []
        observation_ids = []
        for collateral in collaterals:
            observation = ''
            prediction = ''
            statement_id = collateral.typeID
            base64_data = base64.b64encode(collateral.collateralContent).decode("utf-8")   
            if statement_id in observation_dict:
                observation = observation_dict[statement_id]['statementText']
                prediction = observation_dict[statement_id]['solutionText']
            collateral_ids.append(collateral.id)
            observation_ids.append(collateral.typeID)
            collateral_data[collateral.id] = {
                'statementText': observation,
                'solutionText': prediction,
                'contentType': collateral.collateralMimeType,
                'content': base64_data
            }
        
        heatmaps = HeatMap.objects.filter(reportID=report_data.pk)
        site_ids = set()
        for heatmap in heatmaps:
            site_ids.add(heatmap.clientSitePageID.id)
        
        topfeatures = TopFeature.objects.filter(reportID=report_data.pk)
        feature_ids = set()
        for topfeature in topfeatures:
            topfeature_id = topfeature.id
            if topfeature.id not in site_ids:
                site_ids.add(topfeature_id)
            feature_id =  topfeature.featureID.id
            if feature_id not in feature_ids:
                feature_ids.add(feature_id)
        
        customerflows = CustomerFlow.objects.filter(reportID=report_data.pk)
        flowpageorders = FlowPageOrder.objects.filter(reportID=report_data.pk)
        
        clientSitePagesAll = ClientSitePage.objects.all()
        client_site_dict = dict()
        for site in clientSitePagesAll:
            client_site_dict[site.id] = site.pageName
        
        custflow_ids, devicetype_ids = [], []
        custflow_dict = dict()
 
        for custflow in customerflows:
            flow_id = custflow.id
            custflow_ids.append(flow_id)
            devicetype_ids.append(custflow.keyDataID.ID)

            flowpage_list = []
            for flowpageorder in flowpageorders:
                cust_flow_id = flowpageorder.customerFlowID.id
                if cust_flow_id == flow_id:
                    site_id = flowpageorder.clientSitePageID.id
                    flowpageorder_dict = {
                        'id': flowpageorder.id,
                        'page_site_name': client_site_dict[site_id],
                        'pageOrder': flowpageorder.pageOrder
                    }
                    flowpage_list.append(flowpageorder_dict)
            
            custflow_dict[flow_id] = {
                'customerflow_id': flow_id,
                'deviceType': custflow.keyDataID.ID,
                'flowPercent': custflow.flowPercent,
                'flowVisitors': custflow.flowVisitors,
                'flowRanking': custflow.flowRanking,
                'flowPageOrderList': flowpage_list
            }
        
        clientsitepages = ClientSitePage.objects.filter(id__in=site_ids)
        site_name_dict = dict()
        for sitepackage in clientsitepages:
            site_name_dict[sitepackage.id] = sitepackage.pageName
        
        mobile_data, desktop_data, tablet_data = ([] for _ in range(3))
        mobile_flow, desktop_flow, tablet_flow = (dict() for _ in range(3))

        keydata = KeyData.objects.filter(ID__in=set(devicetype_ids))
        keyweb_dict = dict()
        for keyweb in keydata:
            keyweb_dict[keyweb.ID] = {
                'keyweb_name': keyweb.name,
                'keyweb_usercnt': keyweb.userCount
            }
        
        for flow in custflow_dict:
            keydata_id = custflow_dict[flow]['deviceType']
            device_name = keyweb_dict[keydata_id]['keyweb_name']
            if device_name == 'Mobile':
                mobile_data.append(custflow_dict[flow])
                mobile_flow['keyweb_data'] = keyweb_dict[keydata_id]
                mobile_flow['flow_data'] = mobile_data
            elif device_name == 'Desktop':
                desktop_data.append(custflow_dict[flow])
                desktop_flow['keyweb_data'] = keyweb_dict[keydata_id]
                desktop_flow['flow_data'] = desktop_data
            elif device_name == 'Tablet':
                tablet_data.append(custflow_dict[flow])
                tablet_flow['keyweb_data'] = keyweb_dict[keydata_id]
                tablet_flow['flow_data'] = tablet_data
        
        visual_flow = {
            'mobile_flow_data': mobile_flow,
            'desktop_flow_data': desktop_flow,
            'tablet_flow_data': tablet_flow
        }
    
        site_url_dict = dict()
        for clientsitepage in clientsitepages:            
            site_url_dict[clientsitepage.id] = clientsitepage.pageURL
        
        heatmap_data = []
        for heatmap in heatmaps:
            heatmap_dict = dict()
            collateral_id = heatmap.collateralID
            if collateral_id in collateral_data:
                heatmap_dict['collateral'] = collateral_data[collateral_id]
            
            site_id = heatmap.clientSitePageID.id
            if site_id in site_url_dict:
                print('url: ', site_url_dict[site_id])
                heatmap_dict['site_url'] = site_url_dict[site_id]
            
            heatmap_dict['heatMapRank'] = heatmap.heatMapRank
            heatmap_data.append(heatmap_dict)
        
        collaterals = Collateral.objects.filter(reportID=report_data.pk)
        predictions = Statements.objects.filter(
            reportID=report_data.pk, statementType='PRED', informationType='Site'
        )
        prediction_data = getObservationData(predictions, collaterals)

        featuretypes = FeatureType.objects.filter(id__in=feature_ids)
        featuretype_dict = {}
        for featuretype in featuretypes:
            feature_name = featuretype.featureName.title()
            # print('feature_name - title case', feature_name)
            featuretype_dict[featuretype.id] = {
                'featureName': feature_name,
                'featureDefinition': featuretype.featureDefinition,
                'featureUnit': featuretype.featureUnit
            }
        topfeature_data = []
        for feature in topfeatures:
            feature_dict = {}
            feature_dict['featureName'] = featuretype_dict[feature.featureID.id]['featureName']
            feature_dict['featureDefinition'] = featuretype_dict[feature.featureID.id]['featureDefinition']
            feature_dict['featureDescription'] = feature.featureDescription
            feature_dict['significance'] = feature.significance
            topfeature_data.append(feature_dict)
                
        response_data = {
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod,
            'reportID': report_data.pk,
            'customer_visual_flow': visual_flow,
            'heatmaps': heatmap_data,
            'observations': prediction_data,
            'topfeatures': topfeature_data,
            'subscription': client_data.subscription
        }
        return Response(response_data)


@api_view(['POST'])
def getBehavioralInsights(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])
        
        summary = SummaryInsights.objects.get(reportID=report_data.pk)

        wordcloud = WordCloud.objects.filter(reportID=report_data.pk)
        unigrams, bigrams, trigrams = (dict() for _ in range(3))
        for row in wordcloud:
            if row.metaInfo == 'Unigram':
                unigrams[row.text] = row.frequency
            elif row.metaInfo == 'Bigram':
                bigrams[row.text] = row.frequency
            elif row.metaInfo == 'Trigram':
                trigrams[row.text] = row.frequency
        
        wordcloud_data = {
            'unigrams': unigrams,
            'bigrams': bigrams,
            'trigrams': trigrams
        }

        try:
            sentiment = ReviewSentiment.objects.get(reportID=report_data.pk)
            sentiment_predictions = Statements.objects.filter(
                reportID=report_data.pk, statementType='SENTIMENT', informationType='Behavior'
            )
            sentiment_insights = getObservationData(sentiment_predictions)
            sentiment_data = {
                'positive_reviews': sentiment.positiveScore,
                'negative_reviews': sentiment.negativeScore,
                'neutral_reviews': sentiment.neutralScore,
                'sentiment_insights': sentiment_insights
            }
        except ReviewSentiment.DoesNotExist:
            sentiment_data = None

        keyData = KeyData.objects.filter(reportID=report_data.pk)
        channel_data, browser_data, os_data, device_data, social_data = ([] for _ in range(5))
        
        for keyDetail in keyData:
            keyDatail_dict = dict()
            keyDatail_dict['userCount'] = keyDetail.userCount
            keyDatail_dict['revenue'] = keyDetail.revenue
            keyDatail_dict['conversionRate'] = keyDetail.conversionRate
            keyDatail_dict['name'] = keyDetail.name
            
            keydatatype_id = keyDetail.keyDataTypeID.ID
            if keydatatype_id == 2:
                browser_data.append(keyDatail_dict)
            elif keydatatype_id == 3:
                channel_data.append(keyDatail_dict)
            elif keydatatype_id == 4:
                device_data.append(keyDatail_dict)
            elif keydatatype_id == 5:
                os_data.append(keyDatail_dict)
            elif keydatatype_id == 6:
                social_data.append(keyDatail_dict)
        
        key_data = {
            'browser_data': browser_data,
            'channel_data': channel_data,
            'device_data': device_data,
            'os_data': os_data,
            'social_data': social_data
        }
        insights = Statements.objects.filter(
            reportID=report_data.pk, statementType='INSIGHT', informationType='Behavior'
        )
        insight_data = dict()
        for insight in insights:
            insight_data[insight.ID] = insight.statementText
        
        collaterals = Collateral.objects.filter(reportID=report_data.pk)
        predictions = Statements.objects.filter(
            reportID=report_data.pk, statementType='PRED', informationType='Behavior'
        )
        prediction_data = getObservationData(predictions, collaterals)

        clusters = ClusterData.objects.filter(reportID=report_data.pk)
        cluster_data = utils.getClusterData(clusters)
        
        response_data = {
            'companyName': client_data.companyName,
            'from': report_data.fromPeriod,
            'to': report_data.toPeriod,
            'reportID': report_data.pk,
            'revenue': summary.netDollarValue,
            'visits': summary.visitors,
            'conversionRate': summary.currentConversionRate,
            'DXI': summary.DXI,
            'wordcloud': wordcloud_data,
            'sentiment': sentiment_data,
            'insights': insight_data,
            'key_data': key_data,
            'observations': prediction_data,
            'goodCluster': cluster_data,
            'subscription': client_data.subscription
        }        
    return Response(response_data)


@api_view(['POST'])
def getClientReportDates(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        reports = Report.objects.filter(clientID_id = client_data.ID)
        report_dates = dict()
        for report in reports:
            report_status = 'Publish' if report.isApproved else 'Draft'
            report_dates[report.forMonth] = {
                'id': report.pk,
                'from': report.fromPeriod,
                'to': report.toPeriod,
                'status': report_status,
                'subscription': client_data.subscription
            }

    return Response(report_dates)

@api_view(['POST'])
def getStandardSuggestions(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])
        topfeatures = TopFeature.objects.filter(reportID=report_data.pk)
        feature_ids = set()
        feature_suggest_dict, suggestion_dict = [dict() for _ in range(2)]
        for topfeature in topfeatures:
            # topfeature_id = topfeature.id
            # if topfeature.id not in site_ids:
            #     site_ids.add(topfeature_id)
            feature_id =  topfeature.featureID.id
            if feature_id not in feature_ids:
                feature_ids.add(feature_id)
        
        featuretypes = FeatureType.objects.filter(id__in=feature_ids)
        suggestions = FeatureSuggestion.objects.filter(featureID__in=feature_ids)
        print('feature_ids set():', feature_ids, ', suggestions len:', len(suggestions))
        for suggestion in suggestions:
            feature_id = suggestion.featureID.id
            suggestion_text = suggestion.suggestionText
            if feature_id not in suggestion_dict:
                suggestion_dict[feature_id] = list()
                suggestion_dict[feature_id].append(suggestion_text)
            else:
                suggestion_dict[feature_id].append(suggestion_text)
        print(feature_suggest_dict)
        for featuretype in featuretypes:
            feature_name = featuretype.featureName.title()
            feature_id = featuretype.id
            feature_suggest_dict[feature_name] = suggestion_dict[feature_id] if feature_id in suggestion_dict else None
    return Response(feature_suggest_dict)

@api_view(['POST'])
def getVisitorInsights(request):
    if request.method=='POST':
        req_data = JSONParser().parse(request)
        client_data = Client.objects.get(companyName=req_data['companyName'])
        report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=req_data['forMonth'])

        segment_dict, visitors_dict, feature_dict = [dict() for _ in range(3)]
        feature_ids = set()
        visitors = VisitorSegmentation.objects.filter(reportID=report_data.pk)
        seg_features = VisitorSegmentation.objects.filter(reportID=report_data.pk).distinct('featureID')
        seg_metaInfo = VisitorSegmentation.objects.filter(reportID=report_data.pk).distinct('metaInfo')
        for seg in seg_metaInfo:
            meta = seg.metaInfo
            segment_dict[meta] = list()
        print(segment_dict)
        for segment in seg_features:
            feature_ids.add(segment.featureID.id)
        print(feature_ids)
        featuretypes = FeatureType.objects.filter(id__in=feature_ids)
        for feature in featuretypes:
            feature_dict[feature.id] = feature.featureName
        for visitorSegment in visitors:
            metaInfo = visitorSegment.metaInfo
            # userID = visitorSegment.userID
            user_seg = {
                'userID': visitorSegment.userID,
                'featureName': feature_dict[visitorSegment.featureID.id],
                'significance': visitorSegment.significance,
                'compositeDXI': visitorSegment.compositeDXI,
                'userRank': visitorSegment.userRank,
                'metaInfo': visitorSegment.metaInfo
            }
            if metaInfo not in visitors_dict:
                visitors_dict[metaInfo] = list()
                visitors_dict[metaInfo].append(user_seg)
            else:
                visitors_dict[metaInfo].append(user_seg)
        
    return Response(visitors_dict)