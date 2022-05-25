
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewUser(UserCreationForm):
    email=forms.EmailField(label="Email Address",required=True)
    password1=forms.CharField(label='Password',required=True)
    class Meta:
        model=User
        fields=('email','username','password1','password2')