# Week 2 Weekend Build: RAG System

## What is RAG?
Retrieval-Augmented Generation - retrieve relevant docs + generate answers

## Architecture
1. User asks question
2. Embed question (sentence-transformers)
3. Search vector DB (Qdrant)
4. Get top documents
5. Build prompt with context
6. Generate answer (unified LLM)
7. Return response

## Components (already built)
- ✅ Embeddings (Monday-Tuesday)
- ✅ Vector DB (Wednesday)
- ✅ Unified LLM (Thursday)

## Saturday Tasks
- [ ] 8-10 AM: Create RAGSystem class
- [ ] 10-12h: Test basic RAG
- [ ] 12-3 PM: Break
- [ ] 3-5 PM: Add error handling
- [ ] 5-7 PM: Test edge cases

## Sunday Tasks
- [ ] 8-10 AM: Refactor & optimize
- [ ] 10-12h: Break
- [ ] 3-5 PM: Write documentation
- [ ] 5-7 PM: Final commit & push

## Deliverable
Working RAG system that:
- ✅ Stores documents
- ✅ Answers questions using those docs
- ✅ Works with both Ollama and OpenAI
- ✅ Has error handling
- ✅ Well documented