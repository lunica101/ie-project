from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User


def detect_page(request):
    return render(request , 'pages/detection.html')
 
