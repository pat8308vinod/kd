import base64
from ClientManagementService.models import Client
from KeydabraManagerController.models import Report

def getReportData(company, month):
    client_data = Client.objects.get(companyName=company)
    report_data = Report.objects.get(clientID_id=client_data.ID, forMonth=month)
    # print(report_data)
    return client_data, report_data

def getClusterData(clusters):
    city_data, browser_data, channel_data, device_data, os_data, social_data = ([] for _ in range(6))
    for cluster in clusters:
        key_type_id = cluster.keyDataTypeID.ID
        cluster_dict = {
            'name': cluster.name,
            'score': cluster.score
        }
        if key_type_id == 1:
            city_data.append(cluster_dict)
        elif key_type_id == 2:
            browser_data.append(cluster_dict)
        elif key_type_id == 3:
            os_data.append(cluster_dict)
        elif key_type_id == 4:
            channel_data.append(cluster_dict)
        elif key_type_id == 5:
            device_data.append(cluster_dict)
        elif key_type_id == 6:
            social_data.append(cluster_dict)
    
    cluster_data = {
        'city_data': city_data,
        'browser_data': browser_data,
        'os_data': os_data,
        'channel_data': channel_data,
        'device_data': device_data,
        'social_data': social_data
    }
    return cluster_data

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

def getFloatVal(value):
    return float(value) if value is not None else None

def compareValues(value1, value2):
    if value1 is not None and value2 is not None:
        return value1 > value2
    else:
        return None

def sortByMonth(reportIds, summaryInsights):
    index, sortedSummaryList = 0, list()
    for index in range(len(reportIds)):
        for summary in summaryInsights:
            if reportIds[index] == summary.reportID.ID:
                sortedSummaryList.append(summary)
    print('sortedSummaryList: ', sortedSummaryList)
    return sortedSummaryList