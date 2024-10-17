from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')
]
