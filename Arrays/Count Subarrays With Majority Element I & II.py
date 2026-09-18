# 3737. Count Subarrays With Majority Element I

from bisect import bisect_left, insort

class Solution:
    def countMajoritySubarrays(self, nums, target):
        prefix = 0
        ans = 0

        prefixes = [0]

        for num in nums:
            prefix += 1 if num == target else -1

            # Count previous prefix sums less than current prefix
            ans += bisect_left(prefixes, prefix)

            insort(prefixes, prefix)

        return ans

# 3739. Count Subarrays With Majority Element II

from bisect import bisect_left, insort

class Solution:
    def countMajoritySubarrays(self, nums, target):
        prefix = 0
        ans = 0
        prefixes = [0]

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bisect_left(prefixes, prefix)
            insort(prefixes, prefix)

        return ans