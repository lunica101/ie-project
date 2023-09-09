from django.urls import path
from . import views
from app.views import login
from app.views import detect
from app.views import result

urlpatterns = [
    #path('',  login.login_page),
    path('',detect.detect_page),
    path('result/',result.result_page)
]
