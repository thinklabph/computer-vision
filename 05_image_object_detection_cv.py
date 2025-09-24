import os
import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

root_path = os.getcwd()

media_path = os.path.join(root_path, 'media_samples', 'tagisang_robotics.jpg')

media_capture = cv.imread(media_path)

results = model.predict(media_capture)
# results = model.predict(media_capture, classes=[32]) # class 32 is for sports ball
# results = model.predict(media_capture, classes=[0, 32]) # class 0 is for person and class 32 is for sports ball


annotated_frame = results[0].plot()

# annotated_frame = results[0].plot(conf=True, boxes=True, masks=True, labels=True)

cv.imshow('YOLOv11 Detection', annotated_frame)

cv.waitKey(0)

cv.destroyAllWindows()
