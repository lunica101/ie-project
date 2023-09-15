from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from app.forms import ImageDetectionForm , ImageSummaryForm

def result_page(request):
    return render(request, 'pages/showresult.html')
"""
user ส่งข้อมูลไม่ครบทำยังไง
โยนรูปจาก htmlไปเก็บที่folder
"""
