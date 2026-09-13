# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])