import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

media_capture = cv.VideoCapture(0)

while media_capture.isOpened():
    ret, frame = media_capture.read()
    if not ret:
        break

    results = model.predict(frame)
    # results = model.predict(frame, conf=0.5)  # Set a confidence threshold (e.g., 0.5)

    annotated_frame = results[0].plot()

    cv.imshow('YOLOv11 Detection', annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

media_capture.release()
cv.destroyAllWindows()
