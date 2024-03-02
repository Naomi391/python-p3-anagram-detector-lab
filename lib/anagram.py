class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matched_anagrams = []
        for other_word in word_list:
            if sorted(self.word.lower()) == sorted(other_word.lower()):
                matched_anagrams.append(other_word)
        return matched_anagrams
