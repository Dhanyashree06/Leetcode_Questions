# 3699. Number of ZigZag Arrays I

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Length 2
        up = [0] * (m + 1)
        down = [0] * (m + 1)

        for v in range(1, m + 1):
            up[v] = v - 1          # previous value < v
            down[v] = m - v        # previous value > v

        if n == 2:
            return sum(up[1:] + down[1:]) % MOD

        for _ in range(3, n + 1):
            prefix_down = [0] * (m + 1)
            prefix_up = [0] * (m + 1)

            for i in range(1, m + 1):
                prefix_down[i] = (prefix_down[i - 1] + down[i]) % MOD
                prefix_up[i] = (prefix_up[i - 1] + up[i]) % MOD

            total_up = prefix_up[m]

            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            for v in range(1, m + 1):
                # last move is up: previous value must be smaller
                new_up[v] = prefix_down[v - 1]

                # last move is down: previous value must be larger
                new_down[v] = (total_up - prefix_up[v]) % MOD

            up, down = new_up, new_down

        return (sum(up[1:]) + sum(down[1:])) % MOD


# 3700. Number of ZigZag Arrays II

class Solution:
    MOD = 1_000_000_007

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                r = a[i][k]
                if r == 0:
                    continue
                for j in range(m):
                    res[i][j] = (res[i][j] + r * b[k][j]) % self.MOD
        return res

    def powMul(self, base, exp, res):
        while exp > 0:
            if exp & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            exp >>= 1
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m

        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1
            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]
        dp = self.powMul(u, n - 1, dp)
        ans = 0
        for i in range(size):
            ans = (ans + dp[0][i]) % self.MOD

        return ans