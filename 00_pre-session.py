from ultralytics import YOLO
model_nano = YOLO('yolo11n.pt')
model_small = YOLO('yolo11s.pt')
model_medium = YOLO('yolo11m.pt')
model_large = YOLO('yolo11l.pt')
model_extra_large = YOLO('yolo11x.pt')