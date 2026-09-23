from pathlib import Path
import uuid

from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from PIL import Image
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
RESULT_DIR = BASE_DIR / "results"
UPLOAD_DIR.mkdir(exist_ok=True)
RESULT_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
MAX_FILE_SIZE = 8 * 1024 * 1024

app = Flask(__name__)
app.secret_key = "yolov8-demo-local-key"
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

# Small pretrained model: practical for CPU-only demonstrations.
model = YOLO("yolov8n.pt")


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    result_url = None
    detections = []

    if request.method == "POST":
        file = request.files.get("image")

        if not file or not file.filename:
            flash("Please choose an image first.")
            return redirect(url_for("index"))

        if not allowed_file(file.filename):
            flash("Please upload JPG, JPEG, PNG, or WEBP images.")
            return redirect(url_for("index"))

        image_id = uuid.uuid4().hex
        extension = file.filename.rsplit(".", 1)[1].lower()
        input_path = UPLOAD_DIR / f"{image_id}.{extension}"
        output_name = f"{image_id}_detected.jpg"
        output_path = RESULT_DIR / output_name

        file.save(input_path)

        try:
            with Image.open(input_path) as image:
                image.verify()

            results = model.predict(
                source=str(input_path),
                imgsz=416,
                conf=0.25,
                device="cpu",
                verbose=False,
            )
            result = results[0]
            result.save(filename=str(output_path))

            for box in result.boxes:
                class_id = int(box.cls[0])
                detections.append(
                    {
                        "label": result.names[class_id],
                        "confidence": f"{float(box.conf[0]):.2f}",
                    }
                )

            result_url = url_for("result_file", filename=output_name)
        except Exception as exc:
            flash(f"Could not process the image: {exc}")
        finally:
            input_path.unlink(missing_ok=True)

    return render_template(
        "index.html",
        result_url=result_url,
        detections=detections,
    )


@app.route("/results/<path:filename>")
def result_file(filename):
    return send_from_directory(RESULT_DIR, filename)


@app.errorhandler(413)
def file_too_large(_error):
    flash("The image is too large. Please upload a file smaller than 8 MB.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
