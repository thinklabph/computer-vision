import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

media_capture = cv.VideoCapture(0)

while media_capture.isOpened():
    ret, frame = media_capture.read()
    if not ret:
        break

    results = model(frame, classes=[0, 39])    # 0=person, 39=bottle

    annotated_frame = results[0].plot()

    cv.imshow('YOLOv11 Detection', annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

media_capture.release()
cv.destroyAllWindows()
