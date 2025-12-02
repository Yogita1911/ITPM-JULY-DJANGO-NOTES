from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import RegisterForm
# Create your views here.
def home(request):
    return render(request,'home.html',{'Name':'Yogita'})
# ✅ Register View
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# ✅ Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #login(request, user)
        #return redirect('home')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'login.html')

# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# ✅ Home (Protected)
@login_required
def home_view(request):
    return render(request, 'home.html')

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_page(request):
    return render(request, 'admin.html')
