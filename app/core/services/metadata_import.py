import csv
from core.models import Province, District, HealthFacility, DataSet, DataElement, OpenmrsURL

class ImportMetadata:
    # def __init__(self, file): 
    #     self.file = file
        
        
    # @property
    # def path(self):
    #     return self._path
    
    # @path.setter
    # def path(self, path):
    #     self._path = path
    def import_org_units(self, file): 
        path = '/Users/macbook/dev/echo'
        with open(path + '/'+ file) as csv_file:
            data = csv.reader(csv_file)
            next(data) 
            for row in data:
                province, created = Province.objects.get_or_create(name=row[0])
                district, created = District.objects.get_or_create(name=row[1], province=province)
                healthfacility, created = HealthFacility.objects.get_or_create(id=row[4], name=row[2], district=district)

                province.save()
                district.save()
                healthfacility.save()
                
    
    def import_data_elements(self, file):
        path = '/Users/macbook/dev/echo'
        with open(path + '/'+ file) as csv_file:
            data = csv.reader(csv_file)
            next(data)
            dataSet = DataSet.objects.get(id='EqvSJGIvTjJ')
            for row in data:
                dataElement = DataElement(id=row[0], name=row[1], openmrs=row[2], dataSet=dataSet)
                dataElement.save()
                
    def import_openmrs_urls(self, file):
        path = '/Users/macbook/dev/echo'
        with open(path + '/'+ file) as csv_file:
            data = csv.reader(csv_file)
            next(data)
            for row in data:
                dataSet = DataSet.objects.get(name='ART Optimization')
                openmrs_url = OpenmrsURL.objects.create(
                    province=row[0], instance_name=row[1],
                    uuid=row[2], url=row[3], dataSet=dataSet
                )
                openmrs_url.save()