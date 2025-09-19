import os
import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

root_path = os.getcwd()
media_path = os.path.join(root_path, 'media_samples', 'tagisang_robotics.jpg')

media_capture = cv.imread(media_path)

results = model(media_capture)

annotated_frame = results[0].plot()

cv.imshow('YOLOv11 Detection', annotated_frame)

cv.waitKey(0)

cv.destroyAllWindows()

