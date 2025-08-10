# app.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
import cv2
import numpy as np
import io
import os

app = FastAPI()

# Load Haar cascades included with OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")

def anonymize_image(img: np.ndarray) -> np.ndarray:
    # Work on a copy to be safe
    out = img.copy()
    gray = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

    # Detect faces and plates (parameters tuned for demo; adjust if needed)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

    for (x, y, w, h) in list(faces) + list(plates):
        x1, y1 = max(0, x), max(0, y)
        x2, y2 = min(out.shape[1], x + w), min(out.shape[0], y + h)
        roi = out[y1:y2, x1:x2]
        if roi.size == 0:
            continue
        # choose odd kernel sizes proportional to bbox (must be odd)
        kx = max(3, (w // 3) | 1)
        ky = max(3, (h // 3) | 1)
        if kx % 2 == 0: kx += 1
        if ky % 2 == 0: ky += 1
        out[y1:y2, x1:x2] = cv2.GaussianBlur(roi, (kx, ky), 0)
    return out

@app.get("/")
async def index():
    # Serve the UI
    return FileResponse(os.path.join("static", "index.html"))

@app.post("/process")
async def process_image(file: UploadFile = File(...)):
    contents = await file.read()
    arr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        return {"error": "Couldn't decode image. Upload a valid image file."}
    out = anonymize_image(img)
    success, buf = cv2.imencode(".jpg", out)
    if not success:
        return {"error": "Failed to encode processed image."}
    return StreamingResponse(io.BytesIO(buf.tobytes()), media_type="image/jpeg")
