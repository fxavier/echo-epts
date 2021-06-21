from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, timedelta
import json
from dhis2 import Api
import os

import requests
import csv
from core.models import Province, District, HealthFacility, DataSet, DataElement
from core.services.metadata_import import ImportMetadata
from core.services.art_optimization import ARTOptimization


# # API URL from openmrs

# # TETE SERVER
# API_URL = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/80c1489e-a536-4985-98f7-f9b1ad89f66d'

# # TODO: Dates will be pushid automatically
# # This happen on every 23 of each month
# startDate = datetime.now() - timedelta(days=88)
# endDate = startDate + timedelta(days=30)
# str_startDate = str(startDate.strftime('%Y-%m-%d'))
# str_endDate  = str(endDate.strftime('%Y-%m-%d'))

# months = {'01':'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

# period_description = f'{months[str(endDate.month)]}{endDate.year}'

# params = {
#     'startDate': str_startDate, 
#     'endDate': str_endDate
# }


@shared_task
def load_orgunits():
    orgUnits = ImportMetadata()
    orgUnits.import_org_units('orgUnits_dhis.csv')
                
@shared_task
def load_dataElements():
    dataElements = ImportMetadata()
    dataElements.import_data_elements('dataElements.csv')
    
@shared_task
def load_openmrs_urls(): 
    urls = ImportMetadata()
    urls.import_openmrs_urls('openmrs_urls.csv')
    
                
@shared_task
def get_ped_optimization():
    art_optimization = ARTOptimization()
    art_optimization.get_openmrs_data()    
    
@shared_task
def post_ped_art_optimization():
    art_optimization = ARTOptimization()
    art_optimization.post_ped_art_optimization_to_dhis()
    
    # TODO : check if response status is Created and update sync column to True in DataSetValue and DataElementValue
    # if response.json()['status'] == 'SUCCESS':
    #     dataSetValue = DataSetValue.objects.filter()
    # with open('data.txt', 'w') as json_file:
    #     json.dump(data, json_file)
    