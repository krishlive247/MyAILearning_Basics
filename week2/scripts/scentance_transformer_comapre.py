from sentence_transformers import SentenceTransformer

# Test each model
models = ["all-MiniLM-L6-v2", "all-mpnet-base-v2"]

for model_name in models:
    model = SentenceTransformer(model_name)
    embeddings = model.encode(["Test sentence"])
    print(f"{model_name}: {embeddings.shape} dimensions")