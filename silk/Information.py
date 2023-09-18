from ultralytics import YOLO
import os


def get_yolo_result(path=None, img=None):
    if img is None:
        return {}

    if path is None:
        path = os.getcwd()

    model = YOLO("YoloModel//silk2_EN.pt")
    predict = model.predict(source=img, save=True,
                            show=False, project=path)

    # count each
    result_names = predict[0].names
    classic = predict[0].boxes.cls
    classic = [int(x.item()) for x in classic]

    count = {}
    for name in classic:
        count[result_names[name]] = count.get(result_names[name], 0) + 1

    # accuracy
    accu = predict[0].boxes.conf
    accu = [round(float(x.item()), 2) for x in accu]

    # savedir
    leen = predict[0].save_dir
    a = os.path.basename(img)
    path_direc = os.path.join(leen, a)

    return count, classic, accu, path_direc
