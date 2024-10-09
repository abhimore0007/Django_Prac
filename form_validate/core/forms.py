from django import forms
from django.core import validators

def start_with_A(val):
    x=val[0]
    if x.isdigit():
        raise forms.ValidationError('start with letter')


class MarvelForm(forms.Form):
    name = forms.CharField(validators=[start_with_A])


    # def clean_name(self):
    #     validate_name =self.cleaned_data['name']

    #     if len(validate_name)>5:
    #         raise forms.ValidationError('Enter the Name Less than 5 words')
    
    
        
           
            
           
        

        
    