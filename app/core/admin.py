from django.contrib import admin
from core.models import Province, District, HealthFacility, DataSet, DataElement, OpenmrsURL, \
                        DataSet, PeriodDescription, DataElementValue, TestUS

class DataElementAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = [
        'id',
        'name',
        'openmrs'
        ]
    
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
    
# class DataElementValueAdmin(admin.ModelAdmin):
#     ordering = ['dataElement']
#     list_display = ['id', 'dataElement', 'dataSetValue', 'value', 'synced']

# class PeriodAdmin(admin.ModelAdmin): 
#     ordering = ['ano']
#     list_display = ['ano', 'mes', 'period_desc']
    
class OpenMRSURLAdmin(admin.ModelAdmin):
    ordering = ['province']
    list_display = ['province', 'instance_name', 'uuid', 'url']
    
# class OpenmrsOptimizationAdmin(admin.ModelAdmin):
#     ordering = ['hf', 'period']
#     list_display = [
#         'hf', 
#         'period', 
#         'em_tarv',
#         'elegiveislpvr_geral',
#         'elegiveis_lpvr',
#         'elegiveisdtg_geral',
#         'elegiveisdtg',
#         'dtg_geral',
#         'dtg',
#         'lpvr_geral',
#         'lpvr',
#         'synced'
#     ]

class PeriodDescriptionAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'ano',
        'mes',
        'period_ref',
        'period'
    ]
    
class DataElementValueAdmin(admin.ModelAdmin):
    ordering = ['period']
    list_display = [
        'period',
        'value',
        'dataElement',
        'healthFacility',
        'synced'
    ]

admin.site.register(DataElement, DataElementAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
# admin.site.register(DataElementValue, DataElementValueAdmin)
# admin.site.register(DataSetValue)
# admin.site.register(Ano)
# admin.site.register(Period, PeriodAdmin)
admin.site.register(OpenmrsURL, OpenMRSURLAdmin)
# admin.site.register(OpenmrsOptimization, OpenmrsOptimizationAdmin)
admin.site.register(PeriodDescription)
admin.site.register(DataElementValue, DataElementValueAdmin)
admin.site.register(TestUS)