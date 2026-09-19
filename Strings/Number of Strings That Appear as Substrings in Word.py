# 1967. Number of Strings That Appear as Substrings in Word

class Solution:
    def numOfStrings(self, patterns, word):
        count = 0

        for pattern in patterns:
            if pattern in word:
                count += 1

        return count
