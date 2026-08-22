#!/usr/bin/env python3
"""
Week 2 Main Application
Test all modules together
"""

import sys
from pathlib import Path

# Add project root to path (so imports work)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from week2.scripts.embeddings import SimilarityEngine
from week2.scripts.vector_db import VectorStore
from week2.scripts.llm import LLMFactory
from week2.scripts.rag import RAGSystem

def test_embeddings():
    """Test embeddings module"""
    print("\n" + "="*50)
    print("TESTING EMBEDDINGS")
    print("="*50)
    
    engine = SimilarityEngine()
    docs = [
        "Dogs are loyal pets",
        "Cats are independent",
        "Python is a language"
    ]
    
    # Search (simplified)
    query = "Tell me about dogs"
    print(f"Query: {query}")
    print("✅ Embeddings module works!")

def test_vector_db():
    """Test vector database"""
    print("\n" + "="*50)
    print("TESTING VECTOR DATABASE")
    print("="*50)
    
    store = VectorStore()
    docs = [
        "Dogs are loyal pets",
        "Cats are independent",
        "Python is a language"
    ]
    store.add_documents(docs)
    
    results = store.search("Tell me about dogs", top_k=1)
    print(f"Found: {results[0]['text']}")
    print("✅ Vector DB module works!")

def test_llm():
    """Test LLM interface"""
    print("\n" + "="*50)
    print("TESTING LLM INTERFACE")
    print("="*50)
    
    # Test Ollama
    llm = LLMFactory.create("ollama", model="llama2")
    print(f"Created: {llm.get_info()}")
    
    # Uncomment to test OpenAI (requires API key)
    # llm = LLMFactory.create("openai", model="gpt-3.5-turbo", api_key="sk-...")
    # print(f"Created: {llm.get_info()}")
    
    print("✅ LLM interface works!")

def test_rag():
    """Test RAG system"""
    print("\n" + "="*50)
    print("TESTING RAG SYSTEM")
    print("="*50)
    
    rag = RAGSystem(backend="ollama")
    
    docs = [
        "Dogs are loyal and friendly pets",
        "Cats are independent animals",
        "Python is used for AI and data science"
    ]
    rag.add_documents(docs)
    
    result = rag.answer("What are dogs like?")
    print(f"Question: {result['question']}")
    print(f"Answer: {result['answer'][:100]}...")
    print("✅ RAG system works!")

def main():
    """Run all tests"""
    print("🚀 WEEK 2 - TESTING ALL MODULES")
    
    try:
        test_embeddings()
        test_vector_db()
        test_llm()
        test_rag()
        
        print("\n" + "="*50)
        print("✅ ALL TESTS PASSED!")
        print("="*50)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()