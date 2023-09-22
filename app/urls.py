from django.urls import path

from app.views import detect , result , history

urlpatterns = [
    path('', detect.detect_page),
    path('result/', result.result_page) ,
    path('history', history.history_page)
]