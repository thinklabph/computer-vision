from ultralytics import YOLO
model_nano = YOLO('yolo11n.pt')
model_small = YOLO('yolo11s.pt')
model_medium = YOLO('yolo11m.pt')
model_large = YOLO('yolo11l.pt')
model_extra_large = YOLO('yolo11x.pt')
model_seg_nano = YOLO('yolo11n-seg.pt')
model_yoloe_text_visual_prompt = YOLO('yoloe-11s-seg.pt')
model_yoloe_prompt_free = YOLO('yoloe-11s-seg-pf.pt')