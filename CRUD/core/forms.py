from django import forms
from .models import Marvelform


class Marvel(forms.ModelForm):

    class Meta:
        model = Marvelform
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.TextInput(attrs={'class':'form-control'})
        }

        