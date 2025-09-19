import os
import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

# YOLO11n can detect 80 different classes from the COCO dataset
class_names = model.names
print("Items that the model can detect:")
for class_id, class_name in class_names.items():
    print(f"{class_id}: {class_name}")
