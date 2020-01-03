from django.urls import path
from .views import *

urlpatterns = [
    path('summary/', inventory_summary, name='Inventory-Summary'),
    path('new/', inventory_new, name='Inventory-New'),
    path('categories/main', main_category, name='Main-Categories'),
    path('categories/sub', sub_category, name='Sub-Categories'),
]
