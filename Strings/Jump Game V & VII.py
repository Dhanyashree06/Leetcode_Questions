# 1340. Jump Game V

class Solution:
    def maxJumps(self, arr, d):

        n = len(arr)
        dp = {}

        def dfs(i):

            if i in dp:
                return dp[i]

            ans = 1

            # move right
            for j in range(i + 1, min(n, i + d + 1)):

                # blocked
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + dfs(j))

            # move left
            for j in range(i - 1, max(-1, i - d - 1), -1):

                # blocked
                if arr[j] >= arr[i]:
                    break

                ans = max(ans, 1 + dfs(j))

            dp[i] = ans
            return ans

        return max(dfs(i) for i in range(n))
    

# 1871. Jump Game VII

from collections import deque

class Solution:
    def canReach(self, s, minJump, maxJump):

        n = len(s)

        queue = deque([0])

        farthest = 0

        while queue:

            i = queue.popleft()

            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):

                if s[j] == '0':

                    if j == n - 1:
                        return True

                    queue.append(j)

            farthest = end

        return n == 1