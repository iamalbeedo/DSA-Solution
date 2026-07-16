import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        
        current_max = 0
        
        # Build the initial array by tracking the running maximum and finding its GCD with the current number
        for num in nums:
            current_max = max(current_max, num)
            prefix_gcd.append(math.gcd(num, current_max))
            
        # Group identical values together and organize them from smallest to largest
        prefix_gcd.sort()
        
        total_sum = 0
        left = 0
        right = n - 1
        
        # Pull elements symmetrically from both ends to form pairs; odd center element gets skipped naturally
        while left < right:
            total_sum += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return total_sum