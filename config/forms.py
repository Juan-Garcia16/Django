from django import forms
from django.contrib.auth.models import User

class Regristo(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=40, widget=forms.TextInput(attrs={ 
        'class':'form-control',
        'placeholder': 'Username',
    })) #aplicando clases de bootstrap como si fuera html por medio de diccionarios
    email = forms.EmailField(required=True,
    widget= forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'example@gmail.com'
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    
    password_confirmed = forms.CharField(label='Confirm Password' ,required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))
    
    #Validar nombre de usuario existente
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya existe')

        return username

    # Validar correo electrónico existente
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya está registrado')
        
        return email

    # Validar contraseñas
    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password_confirmed') != cleaned_data.get('password'):
            self.add_error('password_confirmed', 'Las contraseñas no coinciden')

    # Guardar usuario por parte de django
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )