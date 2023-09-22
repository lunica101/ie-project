import os

from ultralytics import YOLO
from django.conf import settings


def get_yolo_result(project=None, img=None):
    if img is None:
        return {}

    if project is None:
        project = settings.YOLO_EXAMPLE_PATH

    model = YOLO(settings.YOLO_MODEL)
    predict = model.predict(source=img, save=True, show=False, project=project, exist_ok=True)

    cls_list = predict[0].boxes.cls
    cls_list = [int(x.item()) for x in cls_list]
    
    accuracy_list = predict[0].boxes.conf
    accuracy_list = [round(float(x.item()), 2) for x in accuracy_list]
    
    diectory = predict[0].save_dir
    image_name = os.path.basename(img)
    diectory = os.path.join(diectory, image_name)

    return cls_list, accuracy_list, diectory
