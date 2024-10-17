from django.shortcuts import render,redirect
from .models import Marvelform
from .forms import Marvel

# Create your views here.

def base(request):
    if request.method == 'POST':
        mf=Marvel(request.POST)
        if mf.is_valid():
            mf.save()
        return redirect('base')
    else:
        mf=Marvel()
        mm=Marvelform.objects.all()
        return render(request,'core/base.html',{'mf':mf,'Marvel':mm})
    


