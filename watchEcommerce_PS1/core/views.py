from django.shortcuts import render,redirect
from .forms import RegisterForm,loginForm,UserEditForm,AdminEditForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
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
    if not request.user.is_authenticated:
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
    else:
        return redirect('login')

def log_out(request):
    logout(request)
    return redirect('base')


def User_Profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                UC=AdminEditForm(request.POST,instance=request.user)
            else:
                UC = UserEditForm(request.POST,instance=request.user)
            if UC.is_valid():
                    UC.save()
                    messages.success(request,'Data edit Successfully')
        else:
            if request.user.is_superuser == True:
                UC=AdminEditForm(request.POST,instance=request.user)
                user=User.objects.all()
            else:
                UC=UserEditForm(instance=request.user)
        return render(request,'core/profile.html',{'UC':UC})
    else:
        return redirect('login')
    

def User_Change_Password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            CP=PasswordChangeForm(user=request.user,data=request.POST)
            if CP.is_valid():
                CP.save()
                update_session_auth_hash(request,CP.user)
                messages.success(request,'Password Change SuccessFully')
                return redirect('changePassword')
        else:
            CP=PasswordChangeForm(user=request.user)
            return render(request,'core/ChangePasswordForm.html',{'CP':CP})
    else:
        return redirect('login')
    

