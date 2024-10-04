from django import forms

class Marvel(forms.Form):
	name = forms.CharField(label='name',label_suffix=" = ",initial='Name')
	mail = forms.EmailField(label_suffix=" = ",initial='Email_ID')
	Password = forms.CharField(label_suffix=" = ",initial='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
	file = forms.FileField(initial='Password')
	
	
    
