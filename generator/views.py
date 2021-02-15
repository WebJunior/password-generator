from django.shortcuts import render
from django.http import HttpResponse
import string
import random


def home(request):
    password_length = range(8, 16)
    data = {
        'password_length': password_length
    }
    return render(request, 'generator/home.html', data)


def password(request):
    generated_password = ''
    characters = string.ascii_lowercase
    length = int(request.GET.get('length', 10))
    length = length if length < 50 else 20

    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase
    if request.GET.get('special_characters'):
        characters += '!@#&*' * 2
    if request.GET.get('numbers'):
        characters += string.digits

    for c in range(length):
        generated_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': generated_password})
