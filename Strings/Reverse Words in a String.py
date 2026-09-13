# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s):

        words = s.split()

        words.reverse()

        return " ".join(words)