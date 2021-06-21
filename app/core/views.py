from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from core.forms import ArtOptimizationForm

from core.models import Province, District, HealthFacility, DataSet, DataElementValue

from django.template.loader import get_template


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'optimization_list'
    model = DataElementValue

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['cheque_devolvido'] = Cheque.objects.all().count()
        # context['cheque_cancelado'] = Cheque.objects.filter(estado_cheque='Cancelado').count()
        # context['cheque_regularizado'] = Cheque.objects.filter(estado_cheque='Regularizado').count()

        return context

    def get_queryset(self):
        return DataElementValue.objects.all()
    
class ArtOptimizationListView(ListView):
    template_name = 'artoptimization_list.html'
    context_object_name = 'filtered_data'
    queryset = DataElementValue.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(ArtOptimizationListView, self).get_context_data(**kwargs)
        context['period'] = DataElementValue.objects.all()


