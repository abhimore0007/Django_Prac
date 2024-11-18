from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,loginForm,UserEditForm,AdminEditForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from .models import Watch,Cart,Customer_Detail
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
            log = loginForm(request, request.POST)
            if log.is_valid():
                Name = log.cleaned_data['username']
                Password = log.cleaned_data['password']
                user = authenticate(username=Name, password=Password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            log = loginForm()
        return render(request, 'core/login_form.html', {'log': log})
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


def User_Password_forgot_Form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Forgot_Pass=SetPasswordForm(user=request.user,data=request.POST)
            if Forgot_Pass.is_valid():
                Forgot_Pass.save()
                update_session_auth_hash(request,Forgot_Pass.user)
                messages.success(request,'Password Change SuccessFully')
                return redirect('Profile')
        else:
            Forgot_Pass=SetPasswordForm(user=request.user)
        return render(request,'core/forgot_Password_Form.html',{'Forgot_Pass':Forgot_Pass})
    else:
        return redirect('Login')
    

def User_categories(request):
    watch_cate=Watch.objects.all()
    return render(request,'core/categories.html',{'watch_cate':watch_cate})

def watch_details(request,id):
    watch_details=Watch.objects.get(pk=id)
    return render(request,'core/watch_details.html',{'watch_details':watch_details})

def Add_To_Cart(request,id):
    if request.user.is_authenticated:
        watch_cart=Watch.objects.get(pk=id)
        user=request.user
        Cart(user=user,product=watch_cart).save()
        return redirect('watchdetails', id)
    else:
        return redirect('login')
    

def view_To_Cart(request):
    if request.user.is_authenticated:
        watch_view=Cart.objects.filter(user=request.user)
        total=0
        delivery_charges=3000
        for viewcart in watch_view:
            total+=(viewcart.product.discounted_price*viewcart.quantity)
        final_price =total+delivery_charges
        return render(request,'core/watch_cart.html',{'watch_view':watch_view,'total':total,'final_price':final_price})
    else:
        return redirect('login')
    

def add_to_quantity(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart, pk=id)
        product.quantity += 1
        product.save()
        return redirect('viewCart')
    else:
        return redirect('login')
    

def delete_to_quantity(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart, pk=id)
        if product.quantity>1:
            product.quantity -= 1
            product.save()
            return redirect('viewCart')
    else:
        return redirect('login')
    

def delete_the_Cart(request,id):
     if request.user.is_authenticated:
         delect_cart= Cart.objects.get(pk=id)
         delect_cart.delete()
         return redirect('viewCart')
     else:
         return redirect('login')
     
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def AddressPage(request):
    return render(request,'core/addresspage.html')

def Address_Add(request):
    return render(request,'core/Address_Add.html')
         





    

