from django import forms
from django.contrib.auth.models import User

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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya existe')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya está registrado')
        
        return email
        
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if User.objects.filter(password=password).exists():
            raise forms.ValidationError("La contraseña ya existe")
        
        return password