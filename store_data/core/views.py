from django.shortcuts import render,redirect
from .forms import MarvelForm
from .models import Marvel
# Create your views here.

def index(request):
    if request.method == 'POST':
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            nm=mf.cleaned_data['name']
            em=mf.cleaned_data['email']
            Marvel(name=nm,email=em).save()
            mf=MarvelForm()
                
    else:
        mf=MarvelForm()
    return render(request,'core/index.html',{'mf':mf})