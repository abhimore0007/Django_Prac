from django import forms
from .models import Marvel


# class MarvelForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()


class MarvelForm(forms.ModelForm):

    class Meta:
        model = Marvel
        fields = ['name','email']
        labels = {'name':'Names'}
        error_messages = {
            'name':{'required':'enter proper name'}
        }

        widgets = {
            'email':forms.PasswordInput()
        }


    
    
        
           
            
           
        

        
    