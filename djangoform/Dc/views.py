from django.shortcuts import render
from .forms import Marvel
# Create your views here.

def batman(request):
    mf= Marvel()
    return render(request,'dc/batman.html',{'mf':mf})

