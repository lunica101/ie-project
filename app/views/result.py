from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User


def result_page(request):
    return render(request, 'pages/showresult.html')