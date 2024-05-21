from django.shortcuts import render, redirect
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.changed_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'کاربر با موفقیت ثبت نام شد.', 'success')
            return redirect('home')
    else:
        form = UserRegisterationForm()
    return render(request, 'user_register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, cd['username', 'password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'کاربر با موفقیت وارد شد.', 'success')
                return redirect('home')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.', 'error')
    else:
        form = UserLoginForm()
    return render(request)


def user_logout(request):
    logout(request)
    messages.success(request, 'کاربر با موفقیت خارج شد.', 'success')
    return redirect('home')
