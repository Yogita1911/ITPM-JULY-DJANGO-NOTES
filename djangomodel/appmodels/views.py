from django.shortcuts import render, redirect
from .models import Emp_Details
from .forms import EmpForm
def Show_emp(request):
    emp = Emp_Details.objects.all()
    return render(request, 'Show_emp.html', {'emp': emp})

def add_employee(request):
# When page first loads → empty form
    form = EmpForm()

    if request.method == "POST": #emp add 
        form = EmpForm(request.POST) # bcoz add emp in forms call post
        if form.is_valid():
            form.save()
            return render(request,'Show_emp.html')
    
    return render(request, 'add.html', {'form': form})
