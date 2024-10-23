from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignupForm,UserEditForm,AdminEditForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User

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
            return redirect('Login')
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
        if request.method == 'POST':
            if request.user.is_superuser == True:
                mf=AdminEditForm(request.POST,instance=request.user)
            else:
                mf = UserEditForm(request.POST,instance=request.user)
            if mf.is_valid():
                    mf.save()
                    messages.success(request,'Data edit Successfully')
        else:
            if request.user.is_superuser == True:
                mf=AdminEditForm(request.POST,instance=request.user)
                user=User.objects.all()
            else:
                user=None
                mf=UserEditForm(instance=request.user)
        return render(request,'core/Profile.html',{'mf':mf,'user':user})
    else:
        return redirect('login')
    
def User_logout(request):
    logout(request)
    return redirect('Login')


# PCF : Password Change Form ( In these form they are display the old and new field )

def PCF(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mf=PasswordChangeForm(user=request.user,data=request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                messages.success(request,'Password Change SuccessFully')
                return redirect('Profile')
        else:
            mf=PasswordChangeForm(user=request.user)
        return render(request,'core/pcf.html',{'mf':mf})
    else:
        return redirect('Login')
    

# SPF : SET Password Form ( In these form they are display only New password field )

def SPF(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mf=SetPasswordForm(user=request.user,data=request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                messages.success(request,'Password Change SuccessFully')
                return redirect('Profile')
        else:
            mf=SetPasswordForm(user=request.user)
        return render(request,'core/spf.html',{'mf':mf})
    else:
        return redirect('Login')