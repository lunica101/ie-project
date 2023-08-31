from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User


def detect_page(request):
    if request.method == 'POST':
        img_input = request.POST.get('img_input',None)
        input_text = request.POST.get('input_text',None)
        print(img_input)
        print(input_text)
        return render(request , 'pages/showresult.html')
    return render(request , 'pages/detection.html')
 