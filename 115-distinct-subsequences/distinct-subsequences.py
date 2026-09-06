class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[j] holds the number of ways to form t[0...j-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to form empty string t
        for char_s in s:
            # Iterate backwards to avoid using updated values from current iteration
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]