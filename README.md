# Edge Detection
Image-processing experiments for Sobel and Canny edge detection, with a Flask
interface for uploading an image.

## Requirements

- Python 3
- `pip`

## Set up the Python environment

From the repository root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the Flask app

With the virtual environment activated and dependencies installed, start the
development server from the repository root:

```bash
python app.py
```

Open <http://127.0.0.1:5000/> in a browser. The upload page and result page are
in `templates/upload.html` and `templates/result.html`. Uploaded files and
outputs are stored under `static/uploads/` and `static/outputs/`.

## Project files

- `app.py` — Flask upload and results routes
- `edge_detection.py` — Sobel and Canny image-processing experiment
- `templates/` — HTML templates used by Flask
- `static/uploads/` — uploaded images
- `static/outputs/` — generated result images
- `requirements.txt` — Python package dependencies
