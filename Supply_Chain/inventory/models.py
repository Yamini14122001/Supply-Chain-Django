from django.db import models

# Create your models here.

class Unit(models.Model):
    unitId = models.AutoField(primary_key=True)
    unitTitle = models.CharField(max_length=20)

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryTitle = models.CharField(max_length=100)

class Inventory(models.Model):
    inventoryId = models.AutoField(primary_key=True)
    inventoryName = models.CharField(max_length=100)
    inventoryDesc = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    catId = models.ForeignKey(Category, on_delete=models.CASCADE)

