"""
Question:
Let’s simulate how an LLM could return a word. Create a simple API that takes an array of words (training data) and a sample word. The API should return the most likely next word for the sample word based on the training data. (Hint: Can you preprocess the training data and use a data structure to store word count frequencies?)

Example 1:
Input:
training_data = ["dog", "eats", "fruit", "regularly", "because", "fruit", "is", "healthy"]
sample_word = "dog"

Output:
"eats"

Answer:
This is the bigram model representation for an LLM. A clean solution uses a nested hash table to store frequencies. 
One edge case we have is if the word doesn't exist; we'll just raise an exception in this case. 
Another edge case is if we have a word with two or more succeeding words having the same frequency. In this case, we'll take the lexicographically larger word as our result.
"""

class LLMSimulation:
    def __init__(self, training_data: list[str]):
        self.training_data = training_data
        self.wordToNextWordToFrequency = self.parse_training_data(self.training_data)
        self.wordToMaxFrequentNextWord = self.build_max_freq(self.wordToNextWordToFrequency)

    def parse_training_data(self, data):
        # algorithm: standard array iteration

        wordToNextWordToFrequency = {}

        # iterate through array
        for i in range(len(data) - 1):
            # process current element
            word = data[i]
            nextWord = data[i + 1]
            nextWordFreq = wordToNextWordToFrequency.get(word, {})
            nextWordFreq[nextWord] = nextWordFreq.get(nextWord, 0) + 1
            wordToNextWordToFrequency[word] = nextWordFreq

        return wordToNextWordToFrequency
        
    def build_max_freq(self, wordToNextWordToFrequency):
        # algorithm: standard array iteration

        wordToMaxFrequentNextWord = {}

        # iterate through array
        for word, nextWordToFreqency in wordToNextWordToFrequency.items():
            # process current element
            maxFreqSeenSoFar = 0
            maxWord = None
            # iterate through array
            for nextWord, freq in nextWordToFreqency.items():
                # process current element
                # condition to stop iterating
                if freq > maxFreqSeenSoFar:
                    # update answer
                    maxFreqSeenSoFar = freq
                    maxWord = nextWord
                elif freq == maxFreqSeenSoFar and nextWord > maxWord: # edge case
                    maxWord = nextWord
            
            wordToMaxFrequentNextWord[word] = maxWord

        return wordToMaxFrequentNextWord
            
    def get_most_likely_next_word(self, sample_word):
        # edge case

        if sample_word not in self.wordToMaxFrequentNextWord:
            raise Exception("Word not in training data")
        
        return self.wordToMaxFrequentNextWord[sample_word]
    
llm_model = LLMSimulation(["dog", "eats", "fruit", "regularly", "because", "fruit" "is", "healthy"])
print(llm_model.get_most_likely_next_word("dog"))
