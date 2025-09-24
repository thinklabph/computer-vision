import os
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

root_path = os.getcwd()
print('root_path:', root_path)

media_path = os.path.join(root_path, 'media_samples', 'tops_cebu.mov')
print('media_path:', media_path)

detect_results_path = os.path.join(root_path, 'detect_results')
print('detect_results_path:', detect_results_path)

model.predict(source=media_path, save=True, project=detect_results_path)
