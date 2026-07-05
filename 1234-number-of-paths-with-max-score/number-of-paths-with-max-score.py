class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7

        # WHAT: dp array initialized with [-1, 0] to represent unreachable cells
        # WHY: Keeping a 2D array of size 2 x n optimizes space complexity to O(n)
        dp = [[[-1, 0] for _ in range(n)] for _ in range(2)]

        # Base case: Starting point 'S'
        dp[(n - 1) % 2][n - 1] = [0, 1]

        for i in range(n - 1, -1, -1):
            curr_row = i % 2
            next_row = (i + 1) % 2

            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue
                
                c = board[i][j]
                if c == 'X':
                    dp[curr_row][j] = [-1, 0]
                    continue

                max_score = -1
                paths = 0

                # Check Down
                if i + 1 < n and dp[next_row][j][0] != -1:
                    max_score = dp[next_row][j][0]
                    paths = dp[next_row][j][1]

                # Check Right
                if j + 1 < n and dp[curr_row][j + 1][0] != -1:
                    if dp[curr_row][j + 1][0] > max_score:
                        max_score = dp[curr_row][j + 1][0]
                        paths = dp[curr_row][j + 1][1]
                    elif dp[curr_row][j + 1][0] == max_score:
                        paths = (paths + dp[curr_row][j + 1][1]) % MOD

                # Check Diagonal Down-Right
                if i + 1 < n and j + 1 < n and dp[next_row][j + 1][0] != -1:
                    if dp[next_row][j + 1][0] > max_score:
                        max_score = dp[next_row][j + 1][0]
                        paths = dp[next_row][j + 1][1]
                    elif dp[next_row][j + 1][0] == max_score:
                        paths = (paths + dp[next_row][j + 1][1]) % MOD

                if max_score == -1:
                    dp[curr_row][j] = [-1, 0]
                else:
                    val = 0 if c == 'E' else int(c)
                    dp[curr_row][j] = [max_score + val, paths]

        final_res = dp[0][0]
        return final_res if final_res[0] != -1 else [0, 0]