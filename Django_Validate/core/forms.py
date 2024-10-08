from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


def clean_name(self):
        validate_name =self.cleaned_data['name']

        if len(validate_name)>5:
            raise forms.ValidationError('Enter the Name Less than 5 words')
        
    