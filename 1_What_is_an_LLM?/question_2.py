"""
Question:
Can you implement softmax from scratch given a list of logits (represented as floating point numbers)?

Formula for softmax:
z_i -> e^(z_i) / sum(e^(z_j))

Example 1:
Input:
logits = [1, 2, 3, 4, 5]

Output:
[0.01166, 0.03168, 0.08613, 0.23412, 0.63641]

Answer:
We can use numpy for an easy solution (this solution utilizes some vectorizing for simplicity)
"""
import numpy as np

def softmax(logits: list[float]) -> list[float]:
    # convert to ndarray first to allow vectorizing

    logits = np.array(logits)
    
    expLogits = np.exp(logits)

    result = expLogits / np.sum(expLogits)

    return result.tolist()

print(softmax([1, 2, 3, 4, 5]))
