from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ['img_input','input_text']
