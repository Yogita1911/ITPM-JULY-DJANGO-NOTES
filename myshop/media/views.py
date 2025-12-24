from django.shortcuts import render
from .models import Products

# Create your views here.
def Product_Details(request):
    Pro = Products.objects.all()
    return render(request,'home.html',{'Pro':Pro})
