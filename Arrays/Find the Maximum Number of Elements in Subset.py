# 3020. Find the Maximum Number of Elements in Subset

from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

      
        if 1 in cnt:
            ones = cnt[1]
            if ones % 2 == 0:
                ans = max(ans, ones - 1)
            else:
                ans = max(ans, ones)

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt.get(cur, 0) >= 2:
                length += 2
                cur = cur * cur

            if cnt.get(cur, 0) == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans 
