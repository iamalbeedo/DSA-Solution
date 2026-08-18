from collections import Counter
from typing import List


class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)

        # Case 1: k == 1
        if k == 1:
            unique_nums = [num for num, count in freq.items() if count == 1]
            return max(unique_nums) if unique_nums else -1

        # Case 2: k == n
        if k == n:
            return max(nums)

        # Case 3: 1 < k < n
        ans = -1
        # Check first element
        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])
        # Check last element
        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans