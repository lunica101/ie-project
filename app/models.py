from django.db import models


class ImageDetection(models.Model):
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ImageSummery(models.Model):
    image_type_choices = ((0, 'HmeeKhor (หมื่ขอ)'),
                          (1, 'Heart (หัวใจ)'),
                          (2, 'HmorNam (หม้อน้ำ)'),
                          (3, 'HmeeRuad (หมื่รวด)'),
                          (4, 'BrokenThread (เส้นยืนขาด)'),
                          (5, 'HitchSilk (ขี้ไหม)'),
                          (6, 'SlackThread (เส้นยืนหย่อน)'))

    image_detect = models.ForeignKey(ImageDetection, on_delete=models.CASCADE)
    image_type = models.IntegerField(
        choices=image_type_choices, null=False, blank=False)
    accuracy = models.FloatField(
        null=False, blank=True, help_text='cof in yolo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
