from django.urls import path
from inventory.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'list', InventoryListView)
router.register(r'api', InventoryItemView)
urlpatterns = router.urls

