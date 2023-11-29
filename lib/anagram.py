# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Convert the word to lowercase and sort its letters
        sorted_word = sorted(self.word)

        # Use list comprehension to find anagrams
        anagrams = [word for word in word_list if sorted(word.lower()) == sorted_word and word.lower() != self.word]

        return anagrams
