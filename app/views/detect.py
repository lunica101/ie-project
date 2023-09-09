from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
import os
from django.conf import settings

def ImageView(request):
    if request.method == 'POST':
        img_input = request.FILES.get('img',None)
        input_text = request.POST.get('input_text',None)

            if img_input.is_valid():
                img_input.save()
                input_text.save()
        else:
            return "save is invalid"
    return render(request , 'pages/detection.html')
        
def DisplayImg(request):
    if request.method == "GET":
        img_input = Image.objects.all()
        return render(request , 'pages/showresult.html')

                

# def detect_page(request):
#     if request.method == 'POST':
#         img_input = request.FILES.get('img',None)
#         input_text = request.POST.get('input_text',None)
#         # print(os.path(file))
#         # Upload file => image path
#         # detection_img, xyxy, position = get_imagej_predict(image path)
#         # Save data => model => write models.py
#         # Model.objects.create(), Model.objects.filter(), Model.objects.all(), Model.objects.last()
#         return render(request , 'pages/showresult.html')
#     return render(request , 'pages/detection.html')
#     print(img_input)
#     print(input_text)

