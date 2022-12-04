from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')

            return redirect('signin')

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cv')
        else:
            messages.info(request, "Invalid username or password")

    return render(request, 'registration/signin.html')


def signout(request): #ToDo
    logout(request)
    return redirect('signin')
