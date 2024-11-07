from ultralytics import YOLO

#load model
model = YOLO("yolov8n.yaml")

#use model
results = model.train(data="config.yaml", epochs=1)