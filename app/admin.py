from django.contrib import admin

from app.models import ImageDetection , ImageSummery


class ImageDetectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'description', 'created_at', 'updated_at']
    search_fields = ['id', 'image', 'description']


class ImageSummeryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_detect', 'image_type', 'accuracy', 'created_at', 'updated_at']
    search_fields = ['id', 'image_detect', 'image_type', 'accuracy']


admin.site.register(ImageDetection, ImageDetectionAdmin)
admin.site.register(ImageSummery, ImageSummeryAdmin)
