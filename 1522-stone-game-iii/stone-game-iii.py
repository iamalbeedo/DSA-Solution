class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i] stores the max relative score advantage starting from index i
        dp = [0] * (n + 1)

        # Bottom-up DP: fill from right to left
        for i in range(n - 1, -1, -1):
            max_advantage = float('-inf')
            current_take_sum = 0

            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    current_take_sum += stoneValue[i + k - 1]
                    net_gain = current_take_sum - dp[i + k]
                    max_advantage = max(max_advantage, net_gain)

            dp[i] = max_advantage

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"