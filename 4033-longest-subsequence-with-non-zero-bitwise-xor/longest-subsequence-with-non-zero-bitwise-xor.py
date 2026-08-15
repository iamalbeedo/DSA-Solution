class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_nonzero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        # Case 1: All elements are 0
        if not has_nonzero:
            return 0
            
        # Case 2: XOR of entire array is non-zero
        if total_xor != 0:
            return len(nums)
            
        # Case 3: XOR is zero, but non-zero elements exist
        return len(nums) - 1