#from week2.vector_db import VectorStore
#from week2.llm import LLMFactory
from week2.scripts.vector_db.vector_store import VectorStore
from week2.scripts.llm import LLMFactory

class RAGSystem:
    def __init__(self, backend="ollama"):
        self.vector_store = VectorStore()
        self.llm = LLMFactory.create(backend)
    
    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
    
    def answer(self, question, top_k=3):
        results = self.vector_store.search(question, top_k)
        context = "\n".join([r["text"] for r in results])
        
        prompt = f"""Based on these documents:
{context}

Answer: {question}"""
        
        response = self.llm.generate(prompt)
        return {
            "question": question,
            "context": context,
            "answer": response
        }