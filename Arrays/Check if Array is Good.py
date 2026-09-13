# 2784. Check if Array is Good



class Solution:
    def isGood(self, nums):

        n = max(nums)

        expected = list(range(1, n + 1))
        expected.append(n)

        nums.sort()

        return nums == expected