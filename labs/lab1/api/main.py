'''
Lab 1

Implement this simple REST endpoint using FastAPI framework.

GET /items/{item_id}

Implement above GET by item_id endpoint and you can return the same integer id set in the {item_id} path.
Implement OpenAPI spec endpoint.
Generate Python API client from the OpenAPI spec.
'''

from fastapi import FastAPI 
from typing import Union

app = FastAPI()

@app.get("/")
async def root():
  return {"message" : "hello world!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
  return {"item_id": item_id}
