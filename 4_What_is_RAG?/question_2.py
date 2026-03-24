"""
Question:

Create a simple Python application that uses the sentence-transformers library and a pre-trained model to accept a list of sentences and return embeddings for each sentence.
"""

from sentence_transformers import SentenceTransformer


def get_embeddings(sentences):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    return embeddings


# Example usage
sentences = ["Hello, how are you?", "What is your name?", "I love programming!"]
embeddings = get_embeddings(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print(f"Sentence: '{sentence}'")
    print(f"Embedding dimension: {len(embedding)}")
    print(f"Embedding: {embedding}\n")
