from django.urls import path
from . import views
from .views import TopFiveDataView, GeneNameSearch
urlpatterns = [
    path('top-five-data/', TopFiveDataView.as_view(), name='top-five-data'),
    path('gene-name-search/<str:gene_name>', GeneNameSearch.as_view(), name= 'gene_name_search')
]