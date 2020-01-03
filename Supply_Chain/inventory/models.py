from django.db import models

class Unit(models.Model):
    unitId = models.AutoField(primary_key=True)
    unitTitle = models.CharField(max_length=20)

class Main_Category(models.Model):
    mainCategoryId = models.AutoField(primary_key=True)
    mainCategoryTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.mainCategoryTitle

class Sub_Category(models.Model):
    subCategoryId = models.AutoField(primary_key=True)
    subCategoryTitle = models.CharField(max_length=100)
    mainCatId = models.ForeignKey(Main_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subCategoryTitle

class Inventory(models.Model):
    inventoryId = models.AutoField(primary_key=True)
    inventoryName = models.CharField(max_length=100)
    inventoryDesc = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    mainCatId = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    subCatId = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.inventoryName
