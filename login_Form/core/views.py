from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# def index(request):
#     if request.method == 'POST':
#         mf=UserCreationForm(request.POST)
#         if mf.is_valid():
#             mf.save()
#             messages.success(request,'Welcome to the Avenger')
#             return redirect('index')
#     else:
#         mf=UserCreationForm()
#     return render(request,'core/index.html',{'mf':mf})

def signup(request):
    if request.method == 'POST':
        mf=SignupForm(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'Welcome to the Avenger')
            return redirect('signup')
    else:
        mf=SignupForm()
    return render(request,'core/signup.html',{'mf':mf})

def User_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf=AuthenticationForm(request,data=request.POST)
            if mf.is_valid():
                u_username=mf.cleaned_data['username']
                u_password=mf.cleaned_data['password']
                user=authenticate(username=u_username,password=u_password)
                if user is not None:
                    login(request,user)
                    return redirect('Profile')
        else:
            mf=AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('Profile')

def User_Profile(request):
    if request.user.is_authenticated:
        return render(request,'core/Profile.html')
    else:
        return redirect('login')
    
def User_logout(request):
    logout(request)
    return render('Login')