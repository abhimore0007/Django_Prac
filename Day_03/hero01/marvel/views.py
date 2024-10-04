from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ironman(request):
    return render(request,'marvel/ironman.html')

def spiderman(request):
    return HttpResponse('i am spiderman')