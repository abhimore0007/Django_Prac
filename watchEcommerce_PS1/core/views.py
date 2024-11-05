from django.shortcuts import render,redirect
from .forms import RegisterForm,loginForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
# Create your views here.

def base(request):
    return render(request,'core/index.html')

def register(request):
    if request.method == 'POST':
        reg=RegisterForm(request.POST)
        if reg.is_valid():
            reg.save()
            messages.success(request,'Registration Successfully !!')
            return redirect('register')
    else:
        reg=RegisterForm()
    return render(request,'core/register_form.html',{'reg':reg})

def user_login(request):
    if request.method == 'POST':
        log=loginForm(request,request.POST)
        if log.is_valid():
            Name=log.cleaned_data['username']
            Password=log.cleaned_data['password']
            user=authenticate(username=Name,password=Password)
            messages.success(request,'Login SuccessFully !!')
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        log=loginForm()
        return render(request,'core/login_form.html',{'log':log})

def log_out(request):
    logout(request)
    return redirect('base')


def user_Profile(request):
    return render(request,'core/profile.html')