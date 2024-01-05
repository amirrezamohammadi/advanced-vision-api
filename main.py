from typing import Union
import os
from fastapi import FastAPI
from ultralytics import YOLO
import json
from utils import *
import base64
from pydantic import BaseModel

class Item(BaseModel):
    image: str

# Load a pretrained YOLOv8n model
model = YOLO('best.pt')

app = FastAPI()


@app.get("/")
def read_root():
    # Define remote image or video URL
    source = 'images/new.jpeg'

    # Run inference on the source
    results = model(source)  # list of Results objects
    result = results[0].tojson()
    jResult = json.loads(result)
    finalResult = formatedResult(jResult)

    return {"result": finalResult}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/predict/")
async def predict(item: Item):
    imgdata = base64.b64decode(item.image)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    # Define remote image or video URL
    source = filename

    # Run inference on the source
    results = model(source)  # list of Results objects
    result = results[0].tojson()
    jResult = json.loads(result)
    finalResult = formatedResult(jResult)


    os.remove("some_image.jpg")
    return {"result": finalResult}
