from django.urls import path

from app.views import detect
from app.views import result

urlpatterns = [
    path('', detect.detect_page),
    path('result/', result.result_page)
]