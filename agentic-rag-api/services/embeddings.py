from sentence_transformers import SentenceTransformer
from qdrant_client.models import PointStruct, VectorParams, Distance
from db.qdrant_client import qdrant_client
from lib.extract_text_from_pdf_blob import extract_text_from_pdf_blob

model = SentenceTransformer('all-MiniLM-L6-v2')

async def upload_embeddings(file_blob):
    if not qdrant_client.collection_exists("my_collection"):
        qdrant_client.create_collection(
            collection_name="my_collection",
            vectors_config=VectorParams(size=100, distance=Distance.COSINE),
        )
    
    document_text = extract_text_from_pdf_blob(file_blob)
    embedding = model.encode(document_text)
    
    point = PointStruct(
        id=1,
        vector=embedding,
        payload={"text": document_text}
    )

    qdrant_client.upsert(
        collection_name="my_collection",
        points=[point]
    )