import tiktoken

# Load encoder for llama2
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")  # Use for estimation

texts = [
    "What is AI?",
    "Machine learning is a subset of artificial intelligence that focuses on the ability of machines to learn from data.",
    "I am learning to build AI systems. This journey is exciting and challenging."
]

for text in texts:
    tokens = encoding.encode(text)
    print(f"Text: {text}")
    print(f"Tokens: {len(tokens)}")
    print(f"Estimate (4 chars/token): {len(text) // 4}")
    print()