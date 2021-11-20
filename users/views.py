from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def loginPage(request):
    if request.user.is_authenticated:

        username = request.user.username
        return redirect('home', username)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home', username)

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('/')


def register(request):
    user_form = CustomUserCreationForm()

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            username = request.POST['username']
            password = request.POST['password1']

            messages.success(request, 'User account was created!')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'user account logged in!')
            return redirect('home', username)

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'form': user_form}
    return render(request, 'users/register.html', context)


def home(request, username):

    context = {
        'username': username
    }
    return render(request, 'users/main.html', context)
