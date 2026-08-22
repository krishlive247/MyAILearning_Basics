# Week 2: Embeddings & RAG System

## Overview

A complete Retrieval-Augmented Generation (RAG) system built from scratch. Combines semantic search with language model generation for intelligent Q&A over custom documents.

## What is RAG?

RAG (Retrieval-Augmented Generation) is a technique that:
1. Retrieves relevant documents using semantic search
2. Adds those documents as context
3. Generates answers using an LLM

**Why it works:**
- More accurate than LLM alone
- Can answer questions about your documents
- Cites sources
- Works with local or cloud LLMs

## Architecture

User Question
↓
Embed Query (sentence-transformers)
↓
Search Vector DB (Qdrant)
↓
Retrieve Top-K Documents
↓
Build Prompt with Context
↓
Generate Answer (LLM)
↓
Return Response


## Components

### 1. Embeddings (`embeddings/`)
- Convert text to semantic vectors
- Uses sentence-transformers pre-trained models
- Captures meaning, not just keywords

### 2. Vector Database (`vector_db/`)
- Stores embeddings efficiently
- Fast similarity search
- Qdrant - lightweight, local, instant results

### 3. Unified LLM Interface (`llm/`)
- Abstract interface for any LLM
- Supports Ollama (local) and OpenAI (cloud)
- Swap backends without changing code

### 4. RAG System (`rag/`)
- Combines all components
- Retrieves documents + generates answers
- Production-ready with error handling

## Usage

### Basic Usage

```python
from week2.rag import RAGSystem

# Create system
rag = RAGSystem(backend="ollama", model="llama2")

# Add documents
documents = [
    "Python is used for AI and data science",
    "Machine learning requires data",
    "RAG systems combine retrieval and generation"
]
rag.add_documents(documents)

# Ask questions
result = rag.answer("What is Python used for?")
print(result["answer"])
```

### Using OpenAI

```python
rag = RAGSystem(
    backend="openai",
    model="gpt-3.5-turbo",
    api_key="sk-..."
)
```

### Batch Questions

```python
questions = [
    "What is Python?",
    "Tell me about machine learning",
    "How does RAG work?"
]
results = rag.batch_answer(questions)
```

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Embeddings | sentence-transformers | Convert text to vectors |
| Vector DB | Qdrant | Store & search embeddings |
| LLM Interface | Abstract class | Flexible backend support |
| Local LLM | Ollama | Run models locally free |
| Cloud LLM | OpenAI API | Access GPT models |

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running (if using local)
ollama serve
```

## Features

- ✅ Semantic document search
- ✅ Multi-document retrieval
- ✅ Context-aware answers
- ✅ Local & cloud LLM support
- ✅ Error handling
- ✅ Batch processing
- ✅ Production-ready code

## Example Outputs

**Query: "What is Python used for?"**


## Testing

```bash
# Run test suite
python week2/scripts/tests/test_rag.py

# Test integration
python week2/scripts/integration_test.py

# Manual test
python week2/scripts/rag/rag_system.py
```

## Learning Outcomes

By building this system you learned:

1. **Embeddings** - How to convert text to vectors that capture meaning
2. **Vector Databases** - How to store and search embeddings efficiently
3. **LLM Interfaces** - How to build flexible abstractions over different backends
4. **RAG Systems** - How to combine retrieval and generation for accurate Q&A
5. **Production Code** - How to write professional, documented, tested code

## Next Steps

- Week 3: RAG Optimization & Evaluation
- Week 4: Production RAG Deployment
- Weeks 5+: Agents, APIs, and Full Systems

## Project Structure

week2/
├── embeddings/ # Embedding and similarity
│ ├── text_similarity.py
│ └── similarity_engine.py
├── vector_db/ # Vector database
│ └── vector_store.py
├── llm/ # LLM abstraction
│ └── llm_interface.py
├── rag/ # RAG system
│ └── rag_system.py
├── tests/ # Test suite
│ └── test_rag.py
├── main.py # Main entry point
├── integration_test.py # Integration tests
└── README.md # This file


## Key Insights

1. **Embeddings capture meaning** - Similar concepts have similar vectors
2. **Vector DBs enable scale** - Search millions of documents in milliseconds
3. **Abstraction matters** - Same code works with different LLM backends
4. **RAG > LLM alone** - Adding retrieval dramatically improves accuracy
5. **Testing is essential** - Edge cases reveal real requirements

## Resources

- Sentence Transformers: https://www.sbert.net/
- Qdrant: https://qdrant.tech/
- OpenAI API: https://openai.com/api/
- Ollama: https://ollama.ai/

## Author

Built as part of the AI Engineer Learning Journey