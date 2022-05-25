from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import CreateNewUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    form=CreateNewUser()
    if request.method=='POST':
        form=CreateNewUser(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:login'))
    return render(request,'App_login/sign_up.html',context={'form':form})


def login_form(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_weather:index'))
    return render(request,'App_login/login.html',context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))