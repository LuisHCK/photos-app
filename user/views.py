from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
