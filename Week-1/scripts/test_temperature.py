import ollama

prompt = "Tell me one interesting fact"

print("=== Temperature 0 (Deterministic) ===")
for i in range(3):
    response = ollama.generate(
        model="llama2",
        prompt=prompt,
        options={"temperature": 0},
        stream=False
    )
    print(f"Run {i+1}: {response['response'][:80]}...")

print("\n=== Temperature 1 (Creative) ===")
for i in range(3):
    response = ollama.generate(
        model="llama2",
        prompt=prompt,
        options={"temperature": 1},
        stream=False
    )
    print(f"Run {i+1}: {response['response'][:80]}...")