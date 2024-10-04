from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def batman(request):
    context={'Superhero':'Batman','hero':'thor'}
    return render(request,'dc/batman.html',context)

def flash(request):
    return HttpResponse('i am flash')