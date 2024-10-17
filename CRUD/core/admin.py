from django.contrib import admin
from .models import Marvelform
# Register your models here.


@admin.register(Marvelform)
class MarvelAdmin(admin.ModelAdmin):
    list_display=['id','name','mail']