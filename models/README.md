# Models

The application uses the pretrained **YOLOv8 Nano (`yolov8n.pt`)** model.

The model is downloaded automatically by the Ultralytics package when the notebook or Flask application first calls:

```python
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
```

The binary model file is not committed to the repository to keep the Git repository small. The Nano model is selected for CPU-friendly inference and portfolio demonstration.
