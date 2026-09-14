# 2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums):

        n = len(nums)
        answer = [0] * n

        total_sum = sum(nums)
        left_sum = 0

        for i in range(n):

            total_sum -= nums[i]   # now total_sum = rightSum[i]

            right_sum = total_sum

            answer[i] = abs(left_sum - right_sum)

            left_sum += nums[i]

        return answer