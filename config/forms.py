from django import forms

class Regristo(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=40, 
    widget=forms.TextInput(attrs={ 
        'class':'form-control',
        'placeholder': 'Username',
        })) #aplicando clases de bootstrap como si fuera html por medio de diccionarios
    email = forms.EmailField(required=True,
    widget= forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'example@gmail.com'
        }))
    password = forms.CharField(required=True,
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
        }))