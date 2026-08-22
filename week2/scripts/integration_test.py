#!/usr/bin/env python3
"""
Integration test: All pieces working together
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from week2.scripts.embeddings import SimilarityEngine
#from week2.scripts.embeddings.similarity_engine import SimilarityEngine
from week2.scripts.vector_db import VectorStore
from week2.scripts.llm import LLMFactory

def integration_test():
    """Test all modules working together"""
    print("\n" + "="*60)
    print("WEEK 2 INTEGRATION TEST")
    print("="*60)
    
    # 1. Setup
    print("\n1️⃣ Setting up components...")
    store = VectorStore()
    llm = LLMFactory.create("ollama", model="llama2")
    
    # 2. Add knowledge base
    print("2️⃣ Adding documents...")
    docs = [
        "Python is a programming language used for AI",
        "Machine learning is a subset of AI",
        "Deep learning uses neural networks",
        "Dogs are loyal pets",
        "Cats are independent animals",
        "RAG systems combine retrieval and generation"
    ]
    store.add_documents(docs)
    
    # 3. Ask questions
    questions = [
        "What is Python used for?",
        "Tell me about pets",
        "How do RAG systems work?"
    ]
    
    print("\n3️⃣ Testing integration...")
    for question in questions:
        # Retrieve relevant documents
        results = store.search(question, top_k=2)
        context = "\n".join([r["text"] for r in results])
        
        # Build prompt
        prompt = f"""Based on: {context}
        
Answer: {question}"""
        
        # Generate response
        answer = llm.generate(prompt)
        
        print(f"\n📌 Q: {question}")
        print(f"📚 Context: {context[:60]}...")
        print(f"💬 A: {answer[:100]}...")
    
    print("\n" + "="*60)
    print("✅ INTEGRATION TEST PASSED!")
    print("="*60)

if __name__ == "__main__":
    integration_test()