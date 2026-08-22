from sentence_transformers import SentenceTransformer
import numpy as np

class SimilarityEngine:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.embeddings = None
    
    def add_documents(self, documents):
        self.documents = documents
        self.embeddings = self.model.encode(documents)
    
    def search(self, query, top_k=3):
        # Search logic here
        pass