from django.urls import path
from core.views import IndexView, ArtOptimizationListView
from core import views


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('art-optimization/', ArtOptimizationListView.as_view(), name='art-optimization'),
    # path('cheque/cancelado/', ChequeCanceladoListView.as_view(), name='cheque-cancelado'),
    # path('cheque/relatorio/', GenerateChequePDF.as_view(), name='cheque-relatorio'),
    # path('cheque/regularizado/', ChequeRegularizadoListView.as_view(), name='cheque-regularizado'),
    # path('cheque-regularizado/relatorio/', GenerateChequeRegularizadoPDF.as_view(), name='cheque-regularizado-relatorio'),
    # path('cheque-cancelado/relatorio/', GenerateChequeCanceladoPDF.as_view(), name='cheque-cancelado-relatorio'),
    # path('celery/', views.celery, name='celery'),
    # path('emitente/relatorio', GenerateEmitentePDF.as_view(), name='emitente-relatorio'),
    # path('emitente/create', views.EmitenteCreateView, name='emitente'),
   ]