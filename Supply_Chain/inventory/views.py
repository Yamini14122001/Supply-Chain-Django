from django.shortcuts import render, redirect
from .models import *

def inventory_summary(request):
    pass
def inventory_new(request):
    pass

def main_category(request):
    if request.method == 'POST':
        edit_category = request.POST.get('add-and-edit-category')
        if edit_category == 'add-category':
            categoryName = request.POST.get('main_category_name')
            category = Main_Category(mainCategoryTitle = categoryName)
            category.save()

    context = {
        'title':'Main Category',
        'mainCat': Main_Category.objects.all(),
    }
    return render(request, 'inventory/main-category.html', context)

def sub_category(request):
    if request.method == 'POST':
        edit_category = request.POST.get('add-and-edit-category')
        if edit_category == 'add-category':
            categoryName = request.POST.get('sub_category_name')
            categorySelect = request.POST.get('catSelect')
            print(categoryName, categorySelect)
    context = {
        'title':'Sub Category',
        'subCat': Sub_Category.objects.all(),
        'mainCat': Main_Category.objects.all(),
    }
    return render(request, 'inventory/sub-category.html', context)