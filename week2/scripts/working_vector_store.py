from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.client = QdrantClient(":memory:")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        # Create collection...
    
    def add_documents(self, documents):
        # Embed and store...
        pass
    
    def search(self, query, top_k=3):
        # Search and return results...
        pass