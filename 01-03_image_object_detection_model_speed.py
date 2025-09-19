import os
import cv2 as cv
from ultralytics import YOLO

model_list = ['yolo11n.pt', 'yolo11s.pt', 'yolo11m.pt', 'yolo11l.pt', 'yolo11x.pt']

root_path = os.getcwd()
media_path = os.path.join(root_path, 'media_samples', 'tagisang_robotics.jpg')
media_capture = cv.imread(media_path)

detect_results_path = os.path.join(root_path, 'detect_results')

for model_name in model_list:
    model = YOLO(model_name)
    print(f'Model: {model_name}')
    # print(f'Parameters: {model.params}')
    print('-------------------------')

    start_time = cv.getTickCount()

    results = model(media_capture, save=True, project=detect_results_path)

    end_time = cv.getTickCount()
    time_taken = (end_time - start_time) / cv.getTickFrequency()
    print(f'Time taken for inference: {time_taken:.4f} seconds')
    print('=========================')



# model = YOLO('yolo11n.pt')



# results = model(media_capture)

# annotated_frame = results[0].plot()

# cv.imshow('YOLOv11 Detection', annotated_frame)

# cv.waitKey(0)

# cv.destroyAllWindows()
