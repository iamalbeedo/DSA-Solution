class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # 1. Calculate the sum of the longest sequential prefix starting at index 0
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
        
        # 2. Store elements in a set for fast lookup
        num_set = set(nums)
        
        # 3. Increment prefix_sum until we find an integer missing from nums
        while prefix_sum in num_set:
            prefix_sum += 1
            
        return prefix_sum