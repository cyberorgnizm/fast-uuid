import uuid
from datetime import datetime
from collections import OrderedDict
from fastapi import FastAPI

app = FastAPI()

# global store for timestamp:uuid key value pair
uuid_store = OrderedDict()

def format_timestamp(dt: datetime):
    """formats datetime object to match timestamp e.g 2021-17-23 18:05:50.1621790270"""
    return dt.strftime("%Y-%M-%d %H:%m:%S.%s")

def generate_response() -> OrderedDict:
    """generates dictionary response for timestamp key and uuid values with latest IDs at the top"""
    key = format_timestamp(datetime.now())
    value = uuid.uuid4().hex
    uuid_store[key] =  value
    uuid_store.move_to_end(key=key, last=False)
    return uuid_store

@app.get("/")
def read_uuid():
    response = generate_response()
    return response