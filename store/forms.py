from dataclasses import field, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(required=True,attrs={'class': 'form-control my-2', 'placeholder':'Enter username'}))
    email = forms.EmailField(widget=forms.TextInput(required=True,attrs={'class': 'form-control my-2', 'placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(required=True,attrs={'class': 'form-control my-2', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(required=True,attrs={'class': 'form-control my-2', 'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']