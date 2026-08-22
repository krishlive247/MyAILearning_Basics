"""
RAG System: Retrieval-Augmented Generation

Combines:
- Vector DB for retrieval (vector_store.py)
- LLM for generation (llm_interface.py)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from week2.scripts.vector_db import VectorStore
from week2.scripts.llm import LLMFactory
from typing import List, Dict, Optional

class RAGSystem:
    """
    Retrieval-Augmented Generation System
    
    Workflow:
    1. User asks question
    2. Search vector DB for relevant docs
    3. Build prompt with context
    4. Generate answer using LLM
    """
    
    def __init__(self, backend: str = "ollama", model: Optional[str] = None, api_key: Optional[str] = None):
        """Initialize RAG system
        
        Args:
            backend: "ollama" or "openai"
            model: Model name (default: llama2 for Ollama, gpt-3.5-turbo for OpenAI)
            api_key: OpenAI API key (if using OpenAI)
        """
        # Setup vector store for retrieval
        self.vector_store = VectorStore()
        
        # Setup LLM for generation
        if backend.lower() == "openai":
            if model is None:
                model = "gpt-3.5-turbo"
            self.llm = LLMFactory.create("openai", model=model, api_key=api_key)
        else:
            if model is None:
                model = "llama2"
            self.llm = LLMFactory.create("ollama", model=model)
        
        self.backend = backend
        self.model = self.llm.get_info()
        print(f"🤖 RAG System initialized with {self.model}")
    
    def add_documents(self, documents: List[str]) -> None:
        """Add documents to knowledge base
        
        Args:
            documents: List of document texts
        """
        self.vector_store.add_documents(documents)
        print(f"✅ Added {len(documents)} documents to knowledge base")
    
    def answer(self, question: str, top_k: int = 3, temperature: float = 0.7) -> Dict:
        """Answer a question using RAG
        
        Args:
            question: The question to answer
            top_k: Number of documents to retrieve
            temperature: LLM temperature (0=deterministic, 1=creative)
        
        Returns:
            Dict with question, context, and answer
        """
        # Step 1: Retrieve relevant documents
        try:
            results = self.vector_store.search(question, top_k=top_k)
        except Exception as e:
            return {
                "question": question,
                "context": "",
                "answer": f"Error retrieving documents: {e}",
                "success": False
            }
        
        if not results:
            return {
                "question": question,
                "context": "",
                "answer": "No relevant documents found in knowledge base.",
                "success": False
            }
        
        # Step 2: Build context from retrieved documents
        context_parts = []
        for i, result in enumerate(results, 1):
            context_parts.append(f"[Document {i}] {result['text']}")
        context = "\n\n".join(context_parts)
        
        # Step 3: Build prompt with context
        system_prompt = """You are a helpful assistant. Answer based on the provided documents.
If the answer is not in the documents, say so clearly.
Be concise and accurate."""
        
        full_prompt = f"""{system_prompt}

Documents:
{context}

Question: {question}

Answer:"""
        
        # Step 4: Generate answer using LLM
        try:
            answer = self.llm.generate(
                full_prompt,
                temperature=temperature
            )
        except Exception as e:
            return {
                "question": question,
                "context": context,
                "answer": f"Error generating answer: {e}",
                "success": False
            }
        
        return {
            "question": question,
            "context": context,
            "answer": answer.strip(),
            "success": True,
            "num_documents": len(results)
        }
    
    def batch_answer(self, questions: List[str], top_k: int = 3) -> List[Dict]:
        """Answer multiple questions
        
        Args:
            questions: List of questions
            top_k: Number of documents to retrieve per question
        
        Returns:
            List of answers
        """
        results = []
        for question in questions:
            result = self.answer(question, top_k=top_k)
            results.append(result)
        return results
    
    def get_stats(self) -> Dict:
        """Get system statistics"""
        return {
            "backend": self.backend,
            "model": self.model,
            "knowledge_base_size": self.vector_store.get_stats()["num_documents"]
        }

def main():
    """Test RAG system"""
    print("\n" + "="*60)
    print("🚀 RAG SYSTEM TEST")
    print("="*60)
    
    # Create RAG system
    rag = RAGSystem(backend="ollama", model="llama2")
    
    # Add knowledge base
    documents = [
        "Python is a high-level programming language known for its simplicity and readability.",
        "Machine learning is a subset of artificial intelligence that focuses on data-driven learning.",
        "Deep learning uses neural networks with multiple layers to process data.",
        "Natural language processing (NLP) is about computers understanding human language.",
        "Dogs are loyal, friendly pets that require regular exercise and care.",
        "Cats are independent animals known for their hunting abilities.",
        "RAG (Retrieval-Augmented Generation) combines document retrieval with LLM generation.",
        "Vector databases store embeddings and enable fast similarity search."
    ]
    rag.add_documents(documents)
    
    # Test questions
    questions = [
        "What is Python used for?",
        "Tell me about machine learning",
        "What are dogs like as pets?",
        "How does RAG work?",
        "What do you know about Elephants?"  # This question is not in the knowledge base
    ]
    
    print("\n📋 Answering questions...\n")
    for question in questions:
        result = rag.answer(question, top_k=2)
        
        print(f"❓ Q: {result['question']}")
        print(f"📚 Context: {result['context'][:100]}...")
        print(f"💬 A: {result['answer'][:150]}...\n")
    
    # Stats
    print("📊 System Stats:")
    print(rag.get_stats())
    
    print("\n" + "="*60)
    print("✅ RAG SYSTEM WORKING!")
    print("="*60)

if __name__ == "__main__":
    main()