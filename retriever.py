from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

# Load data
df = pd.read_csv("data/shl_catalog.csv")
documents = (df['name'] + ". " + df['description']).tolist()
index_to_product = df.to_dict(orient="records")

# Load model and index
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(documents)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def retrieve(query, top_k=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [index_to_product[i] for i in indices[0]]