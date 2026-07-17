import math
import bisect

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        # Track the largest element to know the absolute upper boundary for our sieve calculations
        max_val = max(nums)
        
        # Build a frequency map to record how many times each number appears in the dataset
        counts = [0] * (max_val + 1)
        for x in nums:
            counts[x] += 1
            
        # Set up an array to calculate the exact frequency of pairs that produce a specific GCD value
        exact_gcd_pairs = [0] * (max_val + 1)
        
        # Iterate backwards to filter out contributions from higher multiples using inclusion-exclusion logic
        for i in range(max_val, 0, -1):
            multiples_count = 0
            
            # Sum up frequencies of all numbers in the dataset that are perfectly divisible by 'i'
            for j in range(i, max_val + 1, i):
                multiples_count += counts[j]
                
            # Compute total theoretical pair combinations that share 'i' as a common divisor
            total_pairs_with_divisor = (multiples_count * (multiples_count - 1)) // 2
            
            # Subtract counts belonging to larger multiples of 'i' to isolate pairs where GCD is exactly 'i'
            for j in range(2 * i, max_val + 1, i):
                total_pairs_with_divisor -= exact_gcd_pairs[j]
                
            exact_gcd_pairs[i] = total_pairs_with_divisor
            
        # Accumulate exact pair counts into a running prefix sum array to mark index distribution boundaries
        prefix_sum = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sum[i] = prefix_sum[i - 1] + exact_gcd_pairs[i]
            
        # Map each target query position instantly to its corresponding GCD value using binary searching
        return [bisect.bisect_right(prefix_sum, q) for q in queries]