from sentence_transformers import SentenceTransformer
import numpy as np

def find_similar(query, documents, model, top_k=3):
    """Find most similar documents to query"""
    query_embedding = model.encode(query)
    doc_embeddings = model.encode(documents)
    
    similarities = []
    for i, doc_emb in enumerate(doc_embeddings):
        sim = np.dot(query_embedding, doc_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb))
        similarities.append((documents[i], sim))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]

# Test it
model = SentenceTransformer('all-MiniLM-L6-v2')
documents = [
    "Dogs are loyal animals",
    "The cat sat on the mat",
    "Python is a programming language",
    "I love Python programming"
]

results = find_similar("What are dogs like?", documents, model)
for doc, sim in results:
    print(f"{sim:.3f} - {doc}")