"""
CLI Chat Application with Local LLM

A simple chat interface that connects to a local Ollama model
and persists conversation history to JSON.
"""

import ollama
import json
from datetime import datetime
import sys

def load_history(file="chat_history.json"):
    """Load chat history from JSON file"""
    try:
        with open(file,'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_history(history, file="chat_history.json"):
    """Save chat history to JSON file"""
    with open(file,'w') as f:
        json.dump(history, f, indent=2)

def build_context(history, user_input, system_prompt="You are a helpful assistant.", max_history=5):
    """
    Build the full context including conversation history.
    
    Args:
        history: List of previous messages
        user_input: Current user message
        system_prompt: System instructions for the model
        max_history: Number of previous messages to include
    
    Returns:
        Full context string for the model
    """

    context = system_prompt + "\n\n"

    for msg in history[-max_history:]:
        context += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n\n"

    # Add current user input 
    context += f"User: {user_input}\nAssistant:"

    return context

def main():
    """Main chat loop"""
    print("🤖 Chat with Local LLM (with memory)")
    print("Type 'exit' to quit\n")

    history = load_history()
    if history:
        print(f"[Loaded {len(history)} previous messages]\n")
    
    system_prompt = "You are a helpful assistant."

    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            if user_input.lower() == "clear":
                history = []
                save_history(history)
                print("History cleared.\n")
                continue

            # Build context with history
            context = build_context(history, user_input, system_prompt)

            # Call Ollama
            response = ollama.generate(
                model="llama2",
                prompt=context,
                stream=False
            )
            assistant_response = response['response'].strip()
            print(f"Assistant: {assistant_response}\n")

            # Save to history
            history.append({
                "timestamp": datetime.now().isoformat(),
                "user": user_input,
                "assistant": assistant_response
            })
            save_history(history)
            
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Make sure Ollama server is running: ollama serve\n")


if __name__ == "__main__":
    main()