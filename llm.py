import requests
import os

MISTRAL_API_KEY = os.getenv("rAzCkpPQHdSZLihDtrYEwGoILZ0QXtZG")

def generate_response(query, context_docs):
    context = "\n\n".join([f"{doc['name']}: {doc['description']}" for doc in context_docs])
    prompt = f"""You are a helpful assistant for recommending SHL assessments.

User Query: "{query}"

Based on the following products:
{context}

Suggest the most relevant assessments and explain why."""

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistral-medium",  # or mistral-small
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return response.json()["choices"][0]["message"]["content"]
