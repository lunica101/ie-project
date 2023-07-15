from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User


def login_page(request):
    return render(request, 'pages/login.html')
