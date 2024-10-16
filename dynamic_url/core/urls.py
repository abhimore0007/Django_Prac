from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('about/<id>/<num>',views.about,name='about')
]