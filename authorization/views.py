import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.forms import LoginForm, RegistrationForm


# --------
# Регистрация нового пользователя
def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_app:index')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)

# --------
# Вход в личный кабинет
def login_user(request):
    if request.user.is_authenticated:
        return redirect('main_app:index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            user_finded = User.objects.get(email=email)
            user = authenticate(request, username=user_finded.username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('main_app:index')
        else:
            pass
    else:
        form = LoginForm()
    context = {
    }      
    return render(request, 'login.html', context=context)

# --------
# Выход из личного кабинета
def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect("/")