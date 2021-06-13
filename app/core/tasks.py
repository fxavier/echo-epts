from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, timedelta
import os

import requests
import csv
from core.models import Province, District, HealthFacility, DataSet, DataElement, DataElementValue, DataSetValue

path = '/Users/macbook/dev/echo'

# API URL from openmrs

# TETE SERVER
API_URL = 'http://197.218.241.174:8080/openmrs/ws/rest/v1/reportingrest/dataSet/80c1489e-a536-4985-98f7-f9b1ad89f66d'

# TODO: Dates will be pushid automatically

params = {
    'startDate': '2020-05-21', 
    'endDate': '2020-06-20'
}


@shared_task
def load_orgunits():
    with open(path + '/orgUnits_dhis.csv') as file:
            data = csv.reader(file)
            next(data) 
            for row in data:
                province, created = Province.objects.get_or_create(name=row[0])
                district, created = District.objects.get_or_create(name=row[1], province=province)
                healthfacility, created = HealthFacility.objects.get_or_create(id=row[4], name=row[2], openmrs_name=row[3], district=district)
                
                province.save()
                district.save()
                healthfacility.save()
                
@shared_task
def load_dataElements():
     with open(path + '/dataElements.csv') as file:
            data = csv.reader(file)
            next(data)
            dataSet = DataSet.objects.get(id='EqvSJGIvTjJ')
            for row in data:
                dataElement = DataElement(id=row[0], name=row[1], openmrs=row[2], dataSet=dataSet)
                dataElement.save()
                
@shared_task
def get_ped_optimization():
    response = requests.get(API_URL, params=params, auth=('xavier.nhagumbe', 'Goabtgo1'))
    data = response.json()['rows'][0] 
    orgUnit = HealthFacility.objects.get(name=data['us'])
    str_period = datetime.strptime(params['endDate'], '%Y-%m-%d')
    period = datetime.strftime(str_period, '%Y%m')
    dataSet = DataSet.objects.get(pk='EqvSJGIvTjJ')
    dataSetValue, created = DataSetValue.objects.get_or_create(period=period, dataSet=dataSet, orgUnit=orgUnit) 
    dataSetValue.save()
    
    dts_value = DataSetValue.objects.get(period=period)
    
    em_tarv, created = DataElementValue.objects.get_or_create(
        value=data['em_tarv'],
        dataElement=DataElement.objects.get(openmrs='em_tarv'),
        dataSetValue=dts_value
        )
    
    elegiveislpvr_geral, created = DataElementValue.objects.get_or_create(
        value=data['elegiveislpvr_geral'],
        dataElement=DataElement.objects.get(openmrs='elegiveislpvr_geral'),
        dataSetValue=dts_value
        )
    
    lpvr_geral, created = DataElementValue.objects.get_or_create(
        value=data['lpvr_geral'],
        dataElement=DataElement.objects.get(openmrs='lpvr_geral'),
        dataSetValue=dts_value
        )
    
    elegiveis_lpvr, created = DataElementValue.objects.get_or_create(
        value=data['elegiveis_lpvr'],
        dataElement=DataElement.objects.get(openmrs='elegiveis_lpvr'),
        dataSetValue=dts_value
        )
    
    lpvr, created = DataElementValue.objects.get_or_create(
        value=data['lpvr'],
        dataElement=DataElement.objects.get(openmrs='lpvr'),
        dataSetValue=dts_value
        )
    
    elegiveisdtg_geral, created = DataElementValue.objects.get_or_create(
        value=data['elegiveisdtg_geral'],
        dataElement=DataElement.objects.get(openmrs='elegiveisdtg_geral'),
        dataSetValue=dts_value
        )
    
    dtg_geral, created = DataElementValue.objects.get_or_create(
        value=data['dtg_geral'],
        dataElement=DataElement.objects.get(openmrs='dtg_geral'),
        dataSetValue=dts_value
        )
    
    elegiveisdtg, created = DataElementValue.objects.get_or_create(
        value=data['elegiveisdtg'],
        dataElement=DataElement.objects.get(openmrs='elegiveisdtg'),
        dataSetValue=dts_value
        )
    
    dtg, created = DataElementValue.objects.get_or_create(
        value=data['dtg'],
        dataElement=DataElement.objects.get(openmrs='dtg'),
        dataSetValue=dts_value
        )
    
    em_tarv.save()
    elegiveislpvr_geral.save()
    lpvr_geral.save()
    elegiveis_lpvr.save()
    lpvr.save()
    elegiveisdtg_geral.save()
    dtg_geral.save()
    elegiveisdtg.save()
    dtg.save()            