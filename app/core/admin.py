from django.contrib import admin
from core.models import Province, District, HealthFacility, DataSet, DataElement, DataElementValue, DataSetValue

class DataElementAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id', 'name', 'openmrs', 'dataSet']
    
class DataSetAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id', 'name']
    
class ProvinceAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id', 'name']
    
class DistrictAdmin(admin.ModelAdmin):
    ordering = ['province']
    list_display = ['id', 'name', 'province']
    
class HealthFacilityAdmin(admin.ModelAdmin):
    ordering = ['district']
    list_display = ['id', 'name', 'district']
    
class DataElementValueAdmin(admin.ModelAdmin):
    ordering = ['dataElement']
    list_display = ['id', 'dataElement', 'dataSetValue', 'value']
    
admin.site.register(DataElement, DataElementAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(DataElementValue, DataElementValueAdmin)
admin.site.register(DataSetValue)