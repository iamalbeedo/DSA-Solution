class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Pair each number with its original index and sort by value
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * n
        i = 0
        
        while i < n:
            j = i
            indices = []
            
            # Group elements whose adjacent sorted difference is <= limit
            while j < n and (j == i or sorted_nums[j][0] - sorted_nums[j - 1][0] <= limit):
                indices.append(sorted_nums[j][1])
                j += 1
            
            # Sort original indices to place smallest values in leftmost slots
            indices.sort()
            
            # Reassign values to original indices
            for k in range(len(indices)):
                result[indices[k]] = sorted_nums[i + k][0]
                
            i = j  # Move to the next connected group
            
        return result