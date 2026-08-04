class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        min_val, max_val = min(nums), max(nums)
        num_set = set(nums)
        
        # Collect missing numbers in sorted order
        return [x for x in range(min_val, max_val + 1) if x not in num_set]