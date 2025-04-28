from db.qdrant_client import qdrant_client
from qdrant_client.models import VectorParams, Distance

async def get_collections():
    collections = qdrant_client.get_collections()
    return {"collections": collections}

async def create_collection():
    if not qdrant_client.collection_exists("my_collection"):
        qdrant_client.create_collection(
            collection_name="my_collection",
            vectors_config=VectorParams(size=100, distance=Distance.COSINE),
        )
