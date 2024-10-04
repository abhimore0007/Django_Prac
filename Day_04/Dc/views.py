from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def batman(request):
    context={'Superhero':{'spidy':'spiderman','bat':'batman'},'hero':['abhi','raj','vijay','aakash']}
    return render(request,'dc/batman.html',context)

def flash(request):
    return HttpResponse('i am flash')