from django.forms import ModelForm
from app.models import ImageDetection , ImageSummery
"""
save by form.Form 
ไม่สน databseที่ส่งมาคืออะไร ไม่มี implement validate , import ข้อมูล

save by from.ModelForm
data เทียบ Field ใน class model นั้นๆ implementมาให้

แตก branch จาก dev -> feature form

"""
#saving ImageDetection
class ImageDetectionForm(ModelForm):
    class Meta:
         model = ImageDetection 
         fields = ["image", "description"]

class ImageSummaryForm(ModelForm):
     class Meta:
         model = ImageSummery 
         fields = ["image_detect","image_type","accuracy"]
