from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('about',views.about),
    path('contact',views.contact),
    path('home',views.home),
]