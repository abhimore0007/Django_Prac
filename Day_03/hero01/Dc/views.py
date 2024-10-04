from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def batman(request):
    return render(request,'dc/batman.html')

def flash(request):
    return HttpResponse('i am flash')