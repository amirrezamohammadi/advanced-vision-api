# Advanced Vision API

A small [FastAPI](https://fastapi.tiangolo.com/) service that runs [YOLOv8](https://docs.ultralytics.com/) (Ultralytics) inference and returns a compact summary of detected object classes and their counts.

## What it does

- Loads a custom trained model from `best.pt` at startup.
- **GET /** — Runs inference on a local demo image (`images/new.jpeg`) and returns aggregated detection results.
- **POST /predict/** — Accepts a **base64-encoded** JPEG/PNG image, runs detection, then returns a human-readable string of counts per class (sorted by ascending count).

Example response shape for prediction:

```json
{
  "result": "2 person, 1 car, 1 dog"
}
```

## Requirements

- **Python 3.11** (see `runtime.txt`; CI uses 3.11)
- **Model weights**: place your trained YOLO weights at the project root as `best.pt` (the app loads `YOLO('best.pt')`).
- For **GET /**, add a demo image at `images/new.jpeg` (or adjust `main.py`).

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run the API (development):

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive OpenAPI docs.

### POST /predict/ body

Send JSON with a base64 string (no `data:image/...;base64,` prefix required—raw base64 of the image bytes):

```json
{
  "image": "<base64-encoded image bytes>"
}
```

## Production-style run

The `Procfile` uses Gunicorn with Uvicorn workers (typical for platforms like Heroku):

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Deployment

- **Azure Web App**: `.github/workflows/main_advanced-vision.yml` builds on push to `main`, zips the app, and deploys to the `advanced-vision` App Service (requires the configured publish profile secret in GitHub).
- Adjust app name, slot, or triggers in that workflow if you fork the repo.

## Project layout

| File / folder   | Role |
|-----------------|------|
| `main.py`       | FastAPI app, routes, model load |
| `utils.py`      | Aggregates YOLO JSON into count strings |
| `requirements.txt` | Python dependencies |
| `Procfile`      | Web process for PaaS |
| `runtime.txt`   | Python version hint for hosts that read it |

## License

Add a license file if you intend to open-source this repository.
