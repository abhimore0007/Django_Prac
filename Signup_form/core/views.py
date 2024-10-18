from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        mf=UserCreationForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('index')
    else:
        mf=UserCreationForm()
        return render(request,'core/index.html',{'mf':mf})