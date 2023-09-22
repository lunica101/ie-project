import os
import uuid
import cloudinary
import cloudinary.uploader

from django.shortcuts import render , redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from silk.yolo_result import get_yolo_result

from app.models import ImageDetection , ImageSummery  


def result_page(request):
    img = request.FILES['image']

    fs = FileSystemStorage()
    uuid_hex = uuid.uuid4().hex
    file_path = os.path.join(settings.MEDIA_ROOT, 'temp', uuid_hex, img.name)
    fs.save(file_path, img)
    cls_list, accuracy_list, diectory = get_yolo_result(img=file_path)

    if not cls_list:
        return redirect("/")
    
    cloudinary.config( 
        cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'], 
        api_key=settings.CLOUDINARY_STORAGE['API_KEY'], 
        api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
        secure=True 
    )

    public_id = f'media/detection/{uuid.uuid4().hex[:10]}'
    upload_cloud = cloudinary.uploader.upload(diectory, public_id=public_id)
    
    description = request.POST['description']
    imagedetection = ImageDetection.objects.create(image=upload_cloud['url'], description=description)
    
    for i, cls in enumerate(cls_list):
        accuracy = accuracy_list[i]
        ImageSummery.objects.create(image_detect=imagedetection, image_type=cls, accuracy=accuracy)

    os.remove(diectory)
    os.remove(file_path)
    data = {
        "image" : imagedetection.image,
        "description" :imagedetection.description,
        "summary_list" :ImageSummery.objects.filter(image_detect=imagedetection),   
    }
    
    return render(request, 'pages/showresult.html', data)