from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.client = QdrantClient(":memory:")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client.create_collection(
            collection_name="documents",
            vectors_config=VectorParams(
                size=self.model.get_sentence_embedding_dimension(),
                distance=Distance.COSINE
            )
        )
    
    def add_documents(self, documents):
        # Embed and store...
        embeddings = self.model.encode(documents)
        points = [
            PointStruct(
                id=i,
                vector=embedding,
                payload={"text": doc}
            )
            for i, (doc, embedding) in enumerate(zip(documents, embeddings))
        ]
        self.client.upsert(collection_name="documents", points=points)
    
    def search(self, query, top_k=3):
        # Search and return results...
        query_embedding = self.model.encode([query])
        results = self.client.search(
            collection_name="documents",
            query_vector=query_embedding[0],
            limit=top_k
        )
        return [point.payload for point in results]

    def get_stats(self):
        info = self.client.get_collection(collection_name="documents")
        return {"num_documents": info.points_count}