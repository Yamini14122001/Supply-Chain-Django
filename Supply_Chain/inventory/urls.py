from django.urls import path
from .views import *

urlpatterns = [
    path('inventory/summary', inventory_summary, name='Inventory-Summary'),
    path('inventory/new', inventory_new, name='Inventory-New'),
]
