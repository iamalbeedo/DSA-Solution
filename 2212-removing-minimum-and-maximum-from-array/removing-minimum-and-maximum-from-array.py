class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        cost_front = right + 1

        cost_back = n - left

        cost_both = (left + 1) + (n - right)

        return min(cost_front, cost_back, cost_both)