from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneBcells
from django.http import JsonResponse
from django.views import View
from rest_framework import generics, status
from .serializer import GeneSerialaizer
from rest_framework.views import APIView
from rest_framework.response import Response

class TopFiveDataView(APIView):
    def get(self, request):
        top_five_data = GeneBcells.objects.all().order_by('avg_log2fc_1')[:5]
        data = [
            {
                'gene_name': entry.gene_name,
                'p_avg_val_1': entry.p_val_adj_1,
                'Avg_log2fc_1': entry.avg_log2fc_1,
                'p_avg_val_2': entry.p_val_adj_2,
                'Avg_log2fc_2': entry.avg_log2fc_2,
                'p_avg_val_3': entry.p_val_adj_3,
                'Avg_log2fc_3': entry.avg_log2fc_3,
                'p_avg_val_4': entry.p_val_adj_4,
                'Avg_log2fc_4': entry.avg_log2fc_4,
                'p_avg_val_5': entry.p_val_adj_5,
                'Avg_log2fc_5': entry.avg_log2fc_5,               
            }
        
            for entry in top_five_data
        ]
        #serializer_class = GeneSerialaizer
        return JsonResponse(data, status = status.HTTP_200_OK, safe= False )
    
class GeneNameSearch(APIView):
    def get(self, request, gene_name):
        try:
            gene_name = GeneBcells.objects.get(gene_name = gene_name)
            serializer = GeneSerialaizer(gene_name)
            return Response(serializer.data)
        except GeneBcells.DoesNotExist:
            return Response({"error": "Gene not found"}, status=status.HTTP_404_NOT_FOUND)