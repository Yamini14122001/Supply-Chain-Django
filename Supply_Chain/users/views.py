from django.shortcuts import render
from inventory.models import *

# Create your views here.
def Home(request):
    context = {
        'title':'Home'
    }
    return render(request, 'users/home.html', context)
