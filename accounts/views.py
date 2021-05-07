from django.shortcuts import render
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f"{user} خوش آمدید", 'success')
                return redirect('shop:home')
        else:
            messages.error(request, 'اطلاعات وارد شده مطابقت ندارد', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'شما با موفقیت خارج شدید', 'warning')
    return redirect('shop:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['username'], cd['password1'])
            user.save()
            messages.success(request, 'ثبت نام شما با موفقیت انجام شذ', 'success')
            login(request, user)
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/user_register.html', {'form': form})
