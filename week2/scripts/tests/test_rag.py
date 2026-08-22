"""
Test suite for RAG system
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from week2.scripts.rag import RAGSystem

def test_empty_query():
    """Test with empty query"""
    print("Testing: Empty query...")
    rag = RAGSystem()
    rag.add_documents(["Test document"])
    
    result = rag.answer("")
    assert not result["success"] or result["answer"]
    print("✅ Passed")

def test_no_documents():
    """Test when no documents match"""
    print("Testing: No matching documents...")
    rag = RAGSystem()
    rag.add_documents(["Python programming"])
    
    result = rag.answer("Tell me about dogs")
    print(f"Result: {result['answer'][:100]}")
    print("✅ Passed")

def test_multiple_questions():
    """Test batch questions"""
    print("Testing: Batch questions...")
    rag = RAGSystem()
    docs = [
        "Python is for programming",
        "Dogs are pets",
        "RAG systems combine retrieval and generation"
    ]
    rag.add_documents(docs)
    
    questions = ["What is Python?", "Tell me about dogs", "What is RAG?"]
    results = rag.batch_answer(questions)
    
    assert len(results) == 3
    assert all(r["success"] for r in results)
    print("✅ Passed")

def test_special_characters():
    """Test with special characters"""
    print("Testing: Special characters...")
    rag = RAGSystem()
    rag.add_documents([
        "C++ is a language with special: @#$%",
        "Email: test@example.com works fine"
    ])
    
    result = rag.answer("What languages are mentioned?")
    print(f"Result: {result['answer'][:100]}")
    print("✅ Passed")

def test_long_document():
    """Test with long documents"""
    print("Testing: Long document...")
    rag = RAGSystem()
    long_doc = " ".join(["This is a test."] * 100)
    rag.add_documents([long_doc])
    
    result = rag.answer("What is this document about?")
    assert result["success"]
    print("✅ Passed")

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("🧪 RAG SYSTEM TESTS")
    print("="*60 + "\n")
    
    tests = [
        test_empty_query,
        test_no_documents,
        test_multiple_questions,
        test_special_characters,
        test_long_document
    ]
    
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ Failed: {e}")
    
    print(f"\n✅ Passed {passed}/{len(tests)} tests")
    print("="*60)

if __name__ == "__main__":
    run_all_tests()