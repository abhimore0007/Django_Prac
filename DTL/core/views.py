from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'dc/base.html')

def about(request):
    return render(request,'dc/about.html')

def contact(request):
    return render(request,'dc/contact.html')

def home(request):
    return render(request, 'dc/home.html')
