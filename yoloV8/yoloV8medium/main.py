import json
from ultralytics import YOLO

# Cargar el modelo preentrenado YOLOv8
model = YOLO('yolov8m.pt')

# Validar con coco128.yaml y filtrar por una clase específica
results = model.val(data='coco128.yaml', classes=[0], save_json=True)


