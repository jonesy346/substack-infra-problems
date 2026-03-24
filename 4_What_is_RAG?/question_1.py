"""
Question:

Given a query embedding, a list of embeddings, and their corresponding labels, return the label of the embedding most similar to the query (using cosine similarity).

Answer:

We'll use the numpy module to implement cosine similarity and the sentence-transformers library to test (this is using the tool from Q2).
"""

import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(embeddingOne, embeddingTwo):
    dot_product = np.dot(embeddingOne, embeddingTwo)
    
    normOne = np.linalg.norm(embeddingOne)
    normTwo = np.linalg.norm(embeddingTwo)

    if normOne == 0 or normTwo == 0:
        return 0.0
    return dot_product / (normOne * normTwo)

def find_most_similar(query_embedding, embeddings, labels):
    max_similarity = -1
    most_similar_label = None

    # iterate through array
    for i in range(len(embeddings)):
        # process current element
        embedding = embeddings[i]
        label = labels[i]
        similarity = cosine_similarity(query_embedding, embedding)
        # condition to stop iterating
        if similarity > max_similarity:
            # update answer
            max_similarity = similarity
            most_similar_label = label

    return most_similar_label

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# A small corpus of labeled concepts
labels = ['car', 'pizza', 'ocean', 'laptop', 'dog']
embeddings = model.encode(labels)

# Query with semantically related words not in the corpus
queries = ['automobile', 'beach', 'puppy', 'computer']
# iterate through array
for query in queries:
    # process current element
    query_embedding = model.encode(query)
    result = find_most_similar(query_embedding, embeddings, labels)
    print(f"Most similar to '{query}': {result}")

# Expected output:
# Most similar to 'automobile': car
# Most similar to 'beach': ocean
# Most similar to 'puppy': dog
# Most similar to 'computer': laptop
