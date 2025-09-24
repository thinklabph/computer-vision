import cv2 as cv
from ultralytics import YOLO

model = YOLO('yoloe-11s-seg.pt')

object_detect_list = ['dark blue chair', 'person wearing jacket']
model.set_classes(object_detect_list)

media_capture = cv.VideoCapture(0)

while media_capture.isOpened():
    ret, frame = media_capture.read()
    if not ret:
        break

    # results = model.predict(frame)
    results = model.predict(frame)

    # Extract detection results
    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in boxes:
                # Get class name
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                
                # Get confidence score
                confidence = float(box.conf[0])
                
                # Get bounding box coordinates (xyxy format)
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                print(f"Object: {class_name}, Confidence: {confidence:.2f}, "
                      f"Coordinates: ({x1:.1f}, {y1:.1f}, {x2:.1f}, {y2:.1f})")
                
    print('-------------------------')

    annotated_frame = results[0].plot()

    cv.imshow('YOLOv11 Detection', annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

media_capture.release()
cv.destroyAllWindows()
