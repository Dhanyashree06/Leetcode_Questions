# 3300. Minimum Element After Replacement With Digit Sum

class Solution:
    def minElement(self, nums):

        def digit_sum(num):
            return sum(int(d) for d in str(num))

        return min(digit_sum(num) for num in nums)