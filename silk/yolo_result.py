from ultralytics import YOLO
import os
from django.conf import settings

def get_yolo_result(path=None, img=None):
    if img is None:
        return {}

    if path is None:
        path = settings.YOLO_EXAMPLE_PATH

    model = YOLO(settings.YOLO_MODEL)
    predict = model.predict(source=img, save=True, show=False, project=path,exist_ok = True)

    classic = predict[0].boxes.cls
    classic = [int(x.item()) for x in classic]
    
    accuracy = predict[0].boxes.conf
    accuracy = [round(float(x.item()), 2) for x in accuracy]
    
    path_direc = predict[0].save_dir
    a = os.path.basename(img)
    path_direc = os.path.join(path_direc, a)

    return classic, accuracy, path_direc #count
