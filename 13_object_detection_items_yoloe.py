import cv2 as cv
from ultralytics import YOLO

model = YOLO('yoloe-11s-seg-pf.pt')

class_names = model.names
print("Items that the model can detect:")
for class_id, class_name in class_names.items():
    print(f"{class_id}: {class_name}")
