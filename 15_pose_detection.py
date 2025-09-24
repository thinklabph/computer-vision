import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n-pose.pt')

media_capture = cv.VideoCapture(0)

while media_capture.isOpened():
    ret, frame = media_capture.read()
    if not ret:
        break

    height, width, channels = frame.shape
    print(f"Frame dimensions: {width}x{height}")

    results = model.predict(frame)
    # results = model.track(frame)

    # Extract detection results
    for result in results:
        for keypoint in result.keypoints:
            xy = result.keypoints.xy    # x and y coordinates
            print(xy)
            xyn = result.keypoints.xyn   # x and y normalized coordinates
            print(xyn)
        
                
        print('-------------------------')
    print('==================')

    annotated_frame = results[0].plot()

    cv.imshow('YOLOv11 Pose Detection', annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

media_capture.release()
cv.destroyAllWindows()

print(f"Frame dimensions: {width}x{height}")
