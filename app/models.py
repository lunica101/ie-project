from django.db import models
#save บน cloudinary
#get value จาก form

class ImageDetection(models.Model):
    image = models.TextField(null=False, blank=False,max_length=255) #รับค่าเป็น img_input
    description = models.TextField(null=True, blank=True) #รับค่าเป็น text_input
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Image id at {self.id}'
    
    class Meta:
        verbose_name = 'ImageDetection'
        verbose_name_plural = verbose_name


class ImageSummery(models.Model):
    image_type_choices = (
        (0, 'HmeeKhor (หมี่ขอ)'),
        (1, 'Heart (หัวใจ)'),
        (2, 'HmorNam (หม้อน้ำ)'),
        (3, 'HmeeRuad (หมี่รวด)'),
        (4, 'BrokenThread (เส้นยืนขาด)'),
        (5, 'HitchSilk (ขี้ไหม)'),
        (6, 'SlackThread (เส้นยืนหย่อน)')
    )

    image_detect = models.ForeignKey(ImageDetection, on_delete=models.CASCADE)
    image_type = models.IntegerField(choices=image_type_choices, null=False, blank=False)
    accuracy = models.FloatField(null=False, blank=True, help_text='cof in yolo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Image Summary at {self.id} result={self.get_image_type_display()} accuracy={self.accuracy}'
    
    class Meta:
        verbose_name = 'ImageSummery'
        verbose_name_plural = verbose_name
