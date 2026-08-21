import math
from typing import List


class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Precompute LCM and sign for all non-empty subsets of coins
        subsets = []
        for mask in range(1, 1 << n):
            subset_lcm = 1
            size = 0
            for i in range(n):
                if (mask >> i) & 1:
                    subset_lcm = math.lcm(subset_lcm, coins[i])
                    size += 1

            # Inclusion-Exclusion sign: +1 for odd size, -1 for even size
            sign = 1 if size % 2 == 1 else -1
            subsets.append((subset_lcm, sign))

        # Helper function to count valid amounts <= x using PIE
        def count_valid(x: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (x // lcm_val)
            return total

        # Binary search for the smallest x such that count_valid(x) >= k
        left = 1
        right = min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_valid(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans