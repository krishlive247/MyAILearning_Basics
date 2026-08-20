# CLI Chat with Local LLM

A simple command-line chat interface powered by a local Ollama LLM model. Features persistent conversation history and context-aware responses.

## Features

- 💬 **Chat Interface** - Simple CLI for talking to a local LLM
- 🧠 **Memory** - Persistent conversation history saved to JSON
- 🔄 **Context Aware** - Remembers last 5 messages for coherent responses
- 🛡️ **Error Handling** - Graceful recovery if Ollama server stops
- 🚀 **Zero Cloud Cost** - Runs entirely locally on your machine

## Prerequisites

- Python 3.11+
- Ollama (https://ollama.ai)
- A model pulled (llama2, mistral, etc.)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/ai-engineer-journey.git
cd ai-engineer-journey
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Start Ollama server:**
```bash
ollama serve
```

5. **Run the chat (in another terminal):**
```bash
python chat.py
```

## Usage

```bash
python chat.py
```

**Commands:**
- Type your message and press Enter to chat
- Type `exit` and press Enter to quit
- Type `clear` and press Enter to clear history

**Example:**