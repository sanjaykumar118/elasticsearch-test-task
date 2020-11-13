# Test Task

Create an elasticsearch node, whereever you like.

Add `ELASTICSEARCH_HOST` and `ELASTICSEARCH_PORT` environment variables if host and port are other than `localhost` and `9200`.

To create indices run:
`python create_index.py`

To reindex and update documents run:
`python reindex.py`

To run the web app run:
`uvicorn main:app --reload`

Open the web app swagger doc at: `http://localhost:8000/docs`.
