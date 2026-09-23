# Dataset

## COCO8

This project uses **COCO8**, a small sample of the Microsoft COCO dataset provided by Ultralytics for quick object-detection experiments.

The dataset is downloaded by the notebook only when needed. It is intentionally not committed to this repository to keep the project lightweight.

Dataset documentation:
https://docs.ultralytics.com/datasets/detect/coco8/

Source project:
https://github.com/ultralytics/ultralytics

The notebook uses `requests`, `pathlib`, and `zipfile` to download and extract the dataset into a local working directory.
