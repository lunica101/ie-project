from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User


def detect_page(request):
    if request.method == 'POST':
        image = request.POST.get('image',None)
        description = request.POST.get('description',None)
        print(image)
        print(description)
        return render(request , 'pages/showresult.html')
    return render(request , 'pages/detection.html')
 