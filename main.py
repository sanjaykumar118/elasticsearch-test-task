import os

from typing import Optional

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

elastic = Elasticsearch(
    hosts=os.environ.get("ELASTICSEARCH_HOST", "localhost"),
    port=os.environ.get("ELASTICSEARCH_PORT", "9200")
)


class Document(BaseModel):
    index: str
    payload: dict


@app.post("/")
def create_document(document: Document):
    index = document.index
    payload = document.payload

    try:
        elastic.indices.get(index)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail="Index not found")

    result = elastic.index(index=index, body=payload)

    return result


@app.get("/")
def get_documents(index: str = "*"):
    results = elastic.search(index=index)
    return results
