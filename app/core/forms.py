from django import forms
from django.utils.translation import ugettext as _

from core.models import DataElementValue

class ArtOptimizationForm(forms.ModelForm):
    class Meta:
        model = DataElementValue
        fields = ( 'period', 'value', 'healthFacility', 'dataElement', 'synced') 
        
        label = {     
            'period': _('Period'),
            'value': _('Valor'),
            'healthFacility': _('Health Facility'),
            'dataElement': _('Data Element'),  
            'synced': _('Synced'),
        }
