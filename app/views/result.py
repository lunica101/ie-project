import os
import uuid

from django.shortcuts import render , redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from silk.yolo_result import get_yolo_result
import cloudinary
from app.models import ImageDetection , ImageSummery  
from app.forms import ImageDetectionForm , ImageSummaryForm


CLOUDINARY_URL="cloudinary://121655883511222:06i4Ye93J1noHzqb5NwrbZFyPfU@dwyto1jr4"

def result_page(request):
    img = request.FILES['image']
    # description = request.FILES['description']
    fs = FileSystemStorage()
    uuid_hex = uuid.uuid4().hex
    file_path = os.path.join(settings.MEDIA_ROOT, 'temp', uuid_hex, img.name)
    fs.save(file_path, img)
    classic, accuracy, path_direc = get_yolo_result(img=file_path)

    if not classic:
        return redirect("/") #ย้อนกลับหน้าเดิม
    
    #configuration -> access
    cloudinary.config( 
    cloud_name = "dwyto1jr4", 
    api_key = "121655883511222", 
    api_secret = "06i4Ye93J1noHzqb5NwrbZFyPfU",
    secure = True 
    )

    public_id = f'media/detection/{uuid.uuid4().hex[:10]}'
    upload_cloud = cloudinary.uploader.upload(path_direc,public_id=public_id)
    # print(upload_cloud['url'])
    # print(upload_cloud)
    
    description =request.POST['description']
    #create object and save
    imagedetection = ImageDetection.objects.create(image=upload_cloud['url'], description = description)
    # imagedetection.save()
    
    for i ,cls in enumerate(classic):
        a = accuracy[i]
        ImageSummery.objects.create(image_detect=imagedetection, image_type=cls, accuracy=a )
    os.remove(path_direc)
    os.remove(file_path)
    data = {"image" : imagedetection.image ,
            "summary_list" :ImageSummery.objects.filter(image_detect=imagedetection) ,
            "description" :imagedetection.description}
    
    return render(request, 'pages/showresult.html',data)