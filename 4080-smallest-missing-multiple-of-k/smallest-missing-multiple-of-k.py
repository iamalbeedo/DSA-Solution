from typing import List


class Solution:

    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Store all elements in a set for O(1) lookup
        num_set = set(nums)

        # Iterate through positive multiples of k (k, 2k, 3k, ...)
        multiple = k
        while multiple in num_set:
            multiple += k

        return multiple