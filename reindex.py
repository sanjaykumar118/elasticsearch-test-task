import os
from elasticsearch import Elasticsearch
from elasticsearch import helpers

client = Elasticsearch(
    hosts=os.environ.get("ELASTICSEARCH_HOST", "localhost"),
    port=os.environ.get("ELASTICSEARCH_PORT", "9200")
)

indices = client.indices.get_alias("project_*")

update_body = {
    "script": {
        "inline": "ctx._source.last_updated=new Date()",
        "lang": "painless"
    }
}

for index in indices.keys():
    helpers.reindex(client=client, source_index=index,
                    target_index=index)
    print(f"Reindex: {index}")
    task = client.update_by_query(
        index=index, body=update_body, wait_for_completion=False)
    print(f"Updating document for {index}, task id: {task.get('task')}")
