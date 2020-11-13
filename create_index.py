import os
from elasticsearch import Elasticsearch

elastic = Elasticsearch(
    hosts=os.environ.get("ELASTICSEARCH_HOST", "localhost"),
    port=os.environ.get("ELASTICSEARCH_PORT", "9200")
)

indices = ["project_1", "project_2", "project_3"]

for index in indices:
    elastic.indices.create(index=index)
    print(f"Created index: {index}")
