from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Well-come to my first home page in django")

def login(request):
    return HttpResponse("......Plz Insert your Login id and Password...")