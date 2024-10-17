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
    
def delete(request,id):
    if request.method == 'POST':
        mm=Marvelform.objects.get(pk=id)
        mm.delete()
        return redirect('base')
    
def update(request,id):
    if request.method == 'POST':
        mm=Marvelform.objects.get(pk=id)
        mf=Marvel(request.POST,instance=mm)
        if mf.is_valid():
             mf.save()
    else:
        mm=Marvelform.objects.get(pk=id)
        mf=Marvel(instance=mm)
    return render(request,'core/update.html',{'mf':mf})



