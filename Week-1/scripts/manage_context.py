import ollama

def chat_with_limited_context(model="llama2", max_history=5):
    """Chat while keeping context under control"""
    history = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        # Build context from last N messages
        context = "You are a helpful assistant.\n\n"
        for msg in history[-max_history:]:
            context += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n\n"
        context += f"User: {user_input}\nAssistant:"
        
        # Generate response
        response = ollama.generate(
            model=model,
            prompt=context,
            stream=False
        )
        
        assistant_response = response['response'].strip()
        print(f"Assistant: {assistant_response}\n")
        
        # Save to history
        history.append({
            "user": user_input,
            "assistant": assistant_response
        })
        
        # Show context size
        print(f"[History size: {len(history)} messages]\n")

if __name__ == "__main__":
    chat_with_limited_context()