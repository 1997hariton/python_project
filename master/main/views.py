from django.shortcuts import render
from .forms import ImageForm
from .models import *



def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта','tasks':tasks})

def about(request):
    return render(request, 'main/about.html')

def price(request):
    return render(request, 'main/price.html')

def work(request):
    return render(request, 'main/work.html')

