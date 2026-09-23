# Object Detection with YOLO

A lightweight computer vision project that uses **YOLOv8** to detect and localize multiple objects in images with bounding boxes. The project is designed for CPU-only computers and interview demonstrations, so it uses the small `yolov8n` model and an open-source COCO8 sample dataset.

## Project Highlights

- YOLOv8 object detection with bounding boxes and confidence scores
- CPU-friendly `yolov8n` pretrained model
- Notebook-based workflow for learning and demonstration
- COCO8 open-source sample dataset downloaded only when needed
- Flask web application for uploading an image and viewing detections
- Simple repository structure with no `src/` directory or extra preprocessing modules
- LinkedIn and GitHub links included in the web interface
- Optional webcam-style detection code is included in the notebook for local experiments

## Skills Demonstrated

- YOLO / YOLOv8
- Computer Vision
- Object Detection
- Bounding Boxes
- Confidence Scores
- OpenCV
- Python
- Flask
- Model Inference

## Dataset

This project uses the **COCO8** sample dataset from Ultralytics. COCO8 is a small subset intended for quick experimentation and learning. The notebook downloads it on demand instead of storing the dataset in the repository.

Dataset information: https://docs.ultralytics.com/datasets/detect/coco8/

## Model

The project uses the pretrained **YOLOv8 Nano (`yolov8n.pt`)** model. It is intentionally selected because it is much smaller and more practical for CPU-only development than larger YOLO models.

The model is downloaded automatically by Ultralytics the first time it is used.

## Repository Structure

```text
Object-Detection-with-YOLO/
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── notebooks/
│   ├── 01_yolov8_object_detection.ipynb
│   └── 02_webcam_object_detection.ipynb
│
├── results/
│   └── .gitkeep
│
├── uploads/
│   └── .gitkeep
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── CHANGELOG.md
├── CONTRIBUTE.md
├── requirements.txt
└── README.md
```

## Installation

Python **3.10–3.12** is recommended.

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Notebook

Start Jupyter:

```bash
jupyter notebook
```

Open:

```text
notebooks/01_yolov8_object_detection.ipynb
```

The notebook downloads the lightweight sample data and YOLOv8 Nano model when required.

## Run the Flask Web App

From the repository root:

```bash
python app.py
```

Open the local address shown by Flask, normally:

```text
http://127.0.0.1:5000
```

Upload a JPG, JPEG, PNG, or WEBP image. The application runs YOLOv8 inference and displays the image with bounding boxes.

## CPU / Low-Disk Design

This project does not require a GPU. The default model is YOLOv8 Nano, and inference is performed on CPU. The notebooks download only what is required instead of committing large datasets or model binaries to Git.

If disk space is limited, delete downloaded model/cache files after completing the demonstration. They can be downloaded again automatically.

## Interview Demonstration Flow

1. Explain the object-detection problem.
2. Introduce YOLO and bounding boxes.
3. Show the notebook loading YOLOv8 Nano.
4. Run inference on sample COCO8 images.
5. Explain class labels, confidence scores, and bounding-box coordinates.
6. Open the Flask application.
7. Upload a new image and demonstrate live inference through the browser.
8. Explain why a Nano model and CPU inference were selected for the deployment environment.

## Profiles

**GitHub:** https://github.com/InfinitePraveen

**LinkedIn:** https://www.linkedin.com/in/infinitepraveen/

## License

This project code is provided for learning and portfolio demonstration. The COCO dataset is distributed under its own terms; see the dataset documentation for details.
