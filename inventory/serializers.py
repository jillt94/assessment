from rest_framework import serializers
from .models import *
        
        
class SupplierSerializer(serializers.ModelSerializer): 
    id = serializers.UUIDField(read_only=False, required=False)
    
    class Meta:
        model = Supplier
        fields = ('name')
        

class InventoryListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Inventory
        fields = [
            'name',
            'supplier',
            'availability',
        ]
     
    def to_representation(self, instance):
        supplier = super(InventoryListSerializer, self).to_representation(instance)
        supplier['supplier'] = instance.supplier.name
        return supplier
        
class InventoryItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventory
        fields = '__all__'
        
    def to_representation(self, instance):
        supplier = super(InventoryItemSerializer, self).to_representation(instance)
        supplier['supplier'] = instance.supplier.name
        return supplier
        
        