from typing import List

class Solution:

    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Compute prefix sums
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + stones[i]

        # Base case: taking all stones
        max_diff = pref[-1]

        # Process from right to left (index n-2 down to 1)
        for i in range(n - 2, 0, -1):
            max_diff = max(max_diff, pref[i] - max_diff)

        return max_diff