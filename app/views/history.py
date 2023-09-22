from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from app.models import *
from app.views.detect import *
from app.models import ImageDetection , ImageSummery  
from app.views.result import *

def history_page(request):
    datas =[]
    for image_detection in ImageDetection.objects.all():
        data = {
             "img": image_detection.image,
             "hmeekhor" : ImageSummery.objects.filter(image_detect=image_detection , image_type=0).count(),
             "heart" : ImageSummery.objects.filter(image_detect=image_detection , image_type=1).count(),
             "hmornam" : ImageSummery.objects.filter(image_detect=image_detection , image_type=2).count(),
             "hmeeruad" : ImageSummery.objects.filter(image_detect=image_detection , image_type=3).count(),
             "brokenthread" : ImageSummery.objects.filter(image_detect=image_detection , image_type=4).count(),
             "hitchsilk" : ImageSummery.objects.filter(image_detect=image_detection , image_type=5).count(),
             "slackthread" : ImageSummery.objects.filter(image_detect=image_detection , image_type=6).count(),
        }
        datas.append(data)
    return render(request, 'pages/history.html',{"datas" : datas})
