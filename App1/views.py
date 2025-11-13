from django.shortcuts import render


# Create your views here.
def child1(request):
    return render(request ,'child1.html')
def basefile(request):
    return render(request,'basefile.html')
def header(request):
    return render(request,'header.html')
def child2(request):
    return render(request,'child2.html')
def footer(request):
    return render(request,'footer.html')
def variables(request):
    return render(request,'variables.html',
                  {'Name':'Yogita'})
    
def filters(request):
    return render(request,'filters.html',
                  {'marks':[12,43,54,32,65,76,43]})   
     
