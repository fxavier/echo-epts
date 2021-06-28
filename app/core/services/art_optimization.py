import requests
import json
from datetime import datetime, timedelta
from dhis2 import Api
import csv

from core.models import HealthFacility, DataElement, OpenmrsURL, DataElementValue
                        
                        
class ARTOptimization:
    
    def get_openmrs_optimization(self): 
        startDate = datetime.now() - timedelta(days=37)
        endDate = startDate + timedelta(days=30)
        period = endDate.strftime('%Y%m')
        params = {
            'startDate': str(startDate.strftime('%Y-%m-%d')),
            'endDate': str(endDate.strftime('%Y-%m-%d'))
        }
        
        try:
            API_URL = 'http://197.218.206.34:8080/openmrs/ws/rest/v1/reportingrest/dataSet/3443cd92-c2ea-4932-afa0-b58986476fbb'
            
            response = requests.get(API_URL, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
            json_data = response.json()['rows']
            for data in json_data:
                us = ""
                data_dict = {}
                for key, value in data.items(): 
                    if key == 'id':
                        continue
                    elif key == 'us':
                        us = value
                        continue
                    else:
                        data_dict[key] = value
                        
                for key, value in data_dict.items():
                    dataElement = DataElement.objects.get(openmrs=key)
                    healthFacility = HealthFacility.objects.get(name=us)
                    dataElementValue, created = DataElementValue.objects.get_or_create(
                        period=period,
                        value=value,
                        healthFacility=healthFacility,
                        dataElement=dataElement
                    )
                    dataElementValue.save()
                    
        except requests.exceptions.RequestException as err: 
            print(err, API_URL)
        
 
    # def get_openmrs_data(self): 
    #     openmrs_url = OpenmrsURL.objects.filter(province='Manica', instance_name='emondlane')
    #     startDate = datetime.now() - timedelta(days=37)
    #     endDate = startDate + timedelta(days=30)
    #     period = endDate.strftime('%Y%m')
    #     params = {
    #         'startDate': str(startDate.strftime('%Y-%m-%d')),
    #         'endDate': str(endDate.strftime('%Y-%m-%d'))
    #     }
    #     for openmrs in range(1): #openmrs_url:
    #         try:
    #             # base_url = openmrs.url 
    #             # uuid = openmrs.uuid
    #             API_URL = 'http://41.191.74.42:8080/emondlane/ws/rest/v1/reportingrest/dataSet/3443cd92-c2ea-4932-afa0-b58986476fb' # f'{base_url}{uuid}'
                
    #             response = requests.get(API_URL, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
    #             json_data = response.json()['rows']
    #             for data in json_data:
    #                 us = ""
    #                 data_dict = {}
    #                 for key, value in data.items(): 
    #                     if key == 'id':
    #                         continue
    #                     elif key == 'us':
    #                         us = value
    #                         continue
    #                     else:
    #                         data_dict[key] = value
                            
    #                 for key, value in data_dict.items():
    #                     dataElement = DataElement.objects.get(openmrs=key)
    #                     healthFacility = HealthFacility.objects.get(name=us)
    #                     dataElementValue, created = DataElementValue.objects.get_or_create(
    #                         period=period,
    #                         value=value,
    #                         healthFacility=healthFacility,
    #                         dataElement=dataElement
    #                     )
    #                     dataElementValue.save()
                    
    #         except requests.exceptions.RequestException as err: 
    #             print(err, API_URL)
               
                
    def post_ped_art_optimization_to_dhis(self):
        api = Api('https://dhis2.echomoz.org', 'xnhagumbe', 'Go$btgo1')   
        data = {}
        dataList = []
        
    
        dataElementValue = DataElementValue.objects.filter(synced=False)
        
        for dt in dataElementValue:
            data['dataSet'] = dt.dataElement.dataSet.id
        # data['completeDate'] = datetime.now().strftime('%Y-%m-%d')
        for dt in dataElementValue:
            data['period'] = dt.period
            data['orgUnit'] = dt.healthFacility.id
            dataElements = {
                'dataElement': dt.dataElement.id,
                'value' : dt.value
            }
            dataList.append(dataElements)
        data['dataValues'] = dataList  
        try:
            response = api.post('dataValueSets', json=data)
            print(response.status_code)
            print(response.json()['importCount'])
            print(data)
        
        except requests.exceptions.RequestException as err:
            print(err)
        
       
            