from django.shortcuts import render, get_object_or_404
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .serializers import *
from .models import *


# List view to display inventory name, supplier name, and availability
class InventoryListView(viewsets.ModelViewSet):    
    queryset = Inventory.objects.all()
    serializer_class = InventoryListSerializer
    
    def list(self, request, pk=None):
        queryset = self.queryset.all()
        serializer = InventoryListSerializer(queryset, many=True)
        return Response(serializer.data)
    
# View to display data of all information of the item 
class InventoryItemView(viewsets.ModelViewSet):    
    queryset = Inventory.objects.all()
    serializer_class = InventoryItemSerializer
    
    def retrieve(self, request, pk=None):
        queryset = self.queryset.all()
        supplier = get_object_or_404(queryset, pk=pk)  
        serializer = InventoryItemSerializer(supplier)
        return Response(serializer.data)
    