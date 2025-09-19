import os                       # Import the os module for operating system interface functions
import cv2 as cv                # Import OpenCV library for computer vision operations
from ultralytics import YOLO    # Import YOLO from ultralytics for object detection

# Load the YOLOv11 nano model with pre-trained weights
model = YOLO('yolo11n.pt')

# Get the current working directory path
root_path = os.getcwd()

# Construct the full path to the image file
media_path = os.path.join(root_path, 'media_samples', 'tagisang_robotics.jpg')

# Read the image from the specified path into memory
media_capture = cv.imread(media_path)

# Run object detection on the image using the YOLO model
results = model(media_capture)

# Draw bounding boxes and labels on the image based on detection results
annotated_frame = results[0].plot()

# Display the annotated image in a window titled 'YOLOv11 Detection'
cv.imshow('YOLOv11 Detection', annotated_frame)

# Wait for any key press before continuing
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()

