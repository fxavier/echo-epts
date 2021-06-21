import requests
import json
from datetime import datetime, timedelta
from dhis2 import Api
import csv

from core.models import HealthFacility, DataSet, DataElement, OpenmrsURL, DataElementValue, TestUS
                        
                        
class ARTOptimization:
 
    def get_openmrs_data(self): 
        openmrs_url = OpenmrsURL.objects.all()
        startDate = datetime.now() - timedelta(days=31)
        endDate = startDate + timedelta(days=30)
        params = {
            'startDate': str(startDate.strftime('%Y-%m-%d')),
            'endDate': str(endDate.strftime('%Y-%m-%d'))
        }
        for openmrs in openmrs_url:
            base_url = openmrs.url 
            instance_name = openmrs.instance_name
            uuid = openmrs.uuid
            API_URL = f'{base_url}{uuid}'
            try:
                response = requests.get(API_URL, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
                json_data = response.json()['rows']
                for data in json_data:
                    key_list = list(data.keys())
                    val_list = list(data.values())
                    
                    del val_list[8]
                    del val_list[1]
                    key_list.remove('id')
                    key_list.remove('us')
                    data_us = TestUS.objects.create(name=data['us'])
                    data_us.save()
            except requests.exceptions.RequestException as err: 
                print(err, API_URL)
               
                
    def post_ped_art_optimization_to_dhis(self):
        api = Api('https://dhis2sand.echomoz.org', 'xnhagumbe', 'Go$btgo1')   
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
        
       
            