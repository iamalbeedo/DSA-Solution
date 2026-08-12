from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        count_map = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(nums)):
            num = nums[right]
            count_map[num] += 1

            # Shrink window from the left if num appears more than k times
            while count_map[num] > k:
                count_map[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length