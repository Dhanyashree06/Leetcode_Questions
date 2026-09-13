#3120. Count the Number of Special Characters I

class Solution:
    def numberOfSpecialChars(self, word):

        lower = set()
        upper = set()

        for ch in word:

            if ch.islower():
                lower.add(ch)

            else:
                upper.add(ch.lower())

        return len(lower & upper)

# 3121. Count the Number of Special Characters II

class Solution:
    def numberOfSpecialChars(self, word):

        ans = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":

            lower_last = word.rfind(ch)
            upper_first = word.find(ch.upper())

            # both must exist
            if lower_last != -1 and upper_first != -1:

                # all lowercase before uppercase
                if lower_last < upper_first:
                    ans += 1

        return ans