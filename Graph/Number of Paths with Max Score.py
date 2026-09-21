# 1301. Number of Paths with Max Score

class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        dpScore = [[-1] * n for _ in range(n)]
        dpWays = [[0] * n for _ in range(n)]

        dpScore[n - 1][n - 1] = 0
        dpWays[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                ways = 0

                # Down
                if i + 1 < n and dpScore[i + 1][j] != -1:
                    if dpScore[i + 1][j] > best:
                        best = dpScore[i + 1][j]
                        ways = dpWays[i + 1][j]
                    elif dpScore[i + 1][j] == best:
                        ways = (ways + dpWays[i + 1][j]) % MOD

                # Right
                if j + 1 < n and dpScore[i][j + 1] != -1:
                    if dpScore[i][j + 1] > best:
                        best = dpScore[i][j + 1]
                        ways = dpWays[i][j + 1]
                    elif dpScore[i][j + 1] == best:
                        ways = (ways + dpWays[i][j + 1]) % MOD

                # Down-right (reverse of up-left)
                if i + 1 < n and j + 1 < n and dpScore[i + 1][j + 1] != -1:
                    if dpScore[i + 1][j + 1] > best:
                        best = dpScore[i + 1][j + 1]
                        ways = dpWays[i + 1][j + 1]
                    elif dpScore[i + 1][j + 1] == best:
                        ways = (ways + dpWays[i + 1][j + 1]) % MOD

                if best == -1:
                    continue

                value = 0
                if board[i][j].isdigit():
                    value = int(board[i][j])

                dpScore[i][j] = best + value
                dpWays[i][j] = ways % MOD

        if dpScore[0][0] == -1:
            return [0, 0]

        return [dpScore[0][0], dpWays[0][0]]
