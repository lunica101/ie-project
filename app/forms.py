from .models import *
from django import forms

class ImageForm(froms.ModelForm):
    class Meta:
        model = Image
        filed = ['img_input','input_text']