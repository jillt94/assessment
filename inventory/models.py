from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Supplier (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Inventory (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    note = models.TextField(max_length=255)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier')
    
    def __str__(self):
        return self.name
