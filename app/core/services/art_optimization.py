import requests
import json
from datetime import datetime, timedelta
from dhis2 import Api
import csv

from core.models import HealthFacility, DataElement, OpenmrsURL, DataElementValue
                        
                        
class ARTOptimization:
 
    def get_openmrs_data(self): 
        openmrs_url = OpenmrsURL.objects.all()
        startDate = datetime.now() - timedelta(days=34)
        endDate = startDate + timedelta(days=30)
        period = endDate.strftime('%Y%m')
        params = {
            'startDate': str(startDate.strftime('%Y-%m-%d')),
            'endDate': str(endDate.strftime('%Y-%m-%d'))
        }
        for openmrs in openmrs_url:
            try:
                base_url = openmrs.url 
                uuid = openmrs.uuid
                API_URL = f'{base_url}{uuid}'
                
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
        
       
            