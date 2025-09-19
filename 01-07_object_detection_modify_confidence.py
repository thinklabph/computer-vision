import os
import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

root_path = os.getcwd()

media_path = os.path.join(root_path, 'media_samples', 'tops_cebu.mov')

media_capture = cv.VideoCapture(0)

while media_capture.isOpened():
    ret, frame = media_capture.read()
    if not ret:
        break

    results = model(frame, conf=0.6)    # Default confidence is 0.25

    annotated_frame = results[0].plot()

    cv.imshow('YOLOv11 Detection', annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

media_capture.release()
cv.destroyAllWindows()
