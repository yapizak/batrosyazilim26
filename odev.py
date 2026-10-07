import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
img = cv2.imread("img.jpg")
results = model(img)

cv2.imwrite("cikti.jpg", img)