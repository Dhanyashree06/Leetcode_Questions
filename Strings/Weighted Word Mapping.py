# 3838. Weighted Word Mapping

class Solution:
    def mapWordWeights(self, words, weights):
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            rem = total % 26

            # Reverse alphabetical mapping:
            # 0 -> z, 1 -> y, ..., 25 -> a
            ans.append(chr(ord('z') - rem))

        return "".join(ans)