from django.shortcuts import render
from django.shortcuts import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def contact(request):
    return render(request, 'generator/contact.html')