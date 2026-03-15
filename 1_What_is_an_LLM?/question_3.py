"""
One way to convert words to tokens is through a method called Byte Pair Encoding. This algorithm finds the most common pairs of characters in the text and combines them into a new subword until the vocabulary reaches a specified limit. Create a simple API that takes an array of words (training data), vocabulary size, and returns a dictionary containing the vocabulary. (Hint: Can you process the text and use a data structure to store pair count frequencies?)

# Steps:
1. Initialization: Start with each character in the corpus as a separate token:
2. Counting Pair Frequencies: Identify the most frequent adjacent pairs of tokens
3. Merge the Most Frequent Pair 
4. Repeat Steps 2 - 3 until vocabulary size is reached

Example: 

Input:
training_data = ["pan", "pancake"]
vocab_size = 8

Output:
{"p", "a", "n", "c", "k", "e", "pa", "pan"}

Reasoning:
We start with vocabulary = {"p", "a", "n", "c", "k", "e"}. The most frequent pair of characters from the training data is "pa" with frequency 2. We merge "pa" to get {"p", "a", "n", "c", "k", "e", "pa"}. 
Then we count pairs again and find that "pan" is the most frequent pair (comprised of ("pa", "n")) with frequency 2.
"""

def byte_pair_encoding(training_data, vocab_size):
    # initialization
    tokenized = [list(word) for word in training_data]
    vocabulary = set(char for word in training_data for char in word)

    numMerges = vocab_size - len(vocabulary)
    if numMerges <= 0:
        return vocabulary

    # iterate through array
    for _ in range(numMerges):
        # Count Pair Frequencies
        # process current element
        pairToFreq = {}
        
        # iterate through array
        for tokens in tokenized:
            # iterate through array
            for k in range(len(tokens) - 1):
                # process current element
                pair = (tokens[k], tokens[k + 1])
                pairToFreq[pair] = pairToFreq.get(pair, 0) + 1

        if not pairToFreq:
            break

        # find most frequent pair
        maxFreqPair = max(pairToFreq, key=pairToFreq.get)
        merged = maxFreqPair[0] + maxFreqPair[1]

        # merge the most frequent pair across all tokenized words (update the tokenized list)
        # iterate through array
        for j in range(len(tokenized)):
            # process current element
            tokens = tokenized[j]
            new_tokens = []
            k = 0
            # iterate through array
            while k < len(tokens):
                # condition to stop iterating
                if k < len(tokens) - 1 and (tokens[k], tokens[k + 1]) == maxFreqPair:
                    # update answer
                    new_tokens.append(merged)
                    k += 2
                else:
                    new_tokens.append(tokens[k])
                    k += 1
            tokenized[j] = new_tokens

        vocabulary.add(merged)

    return vocabulary

print(byte_pair_encoding(["pan", "pancake"], 8))
