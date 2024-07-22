class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
    
    # Create a list to store tuples of (word, index)
        indexed_words = []
    
    # Iterate over each word in the shuffled sentence
        for word in words:
        # Extract the word and its index
            actual_word = word[:-1]  # Remove the last character (which is the index)
            index = int(word[-1])  # Convert the last character to an integer
        # Append tuple (word, index) to the list
            indexed_words.append((actual_word, index))
    
    # Sort the words based on their indices
        indexed_words.sort(key=lambda x: x[1])
    
    # Extract the words in sorted order
        original_words = [word[0] for word in indexed_words]
    
    # Join the words to form the original sentence
        original_sentence = " ".join(original_words)
    
        return original_sentence