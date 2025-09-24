import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.onnx')

media_capture = cv.VideoCapture(0)

while media_capture.isOpened():
    ret, frame = media_capture.read()
    if not ret:
        break

    results = model.predict(frame)

    annotated_frame = results[0].plot()

    cv.imshow('YOLOv11 Detection', annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

media_capture.release()
cv.destroyAllWindows()
