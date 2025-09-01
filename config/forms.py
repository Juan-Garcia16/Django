from django import forms

class Regristo(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=40)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)