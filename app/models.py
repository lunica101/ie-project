from django.db import models

#create model here

class Image(models.Model):
    img_input = models.ImageField(upload_to='silk/uploadimg',blank=False)
    input_text = models.CharField(blank = False)