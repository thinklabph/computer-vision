import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

# Export the model to ONNX format (optional)
# imgsz can be adjusted based on your requirements, multiples of 32, e.g., 32, 64, 92, 128, 160, 192, 224, 256, etc.
model.export(format='onnx', imgsz=192)
