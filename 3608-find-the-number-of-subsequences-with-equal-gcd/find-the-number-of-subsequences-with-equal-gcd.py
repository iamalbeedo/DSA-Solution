class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # Helper function to find Greatest Common Divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Memoization table to cache results of sub-problems
        # State key: (index, gcd1, gcd2)
        memo = {}

        def solve(idx, g1, g2):
            # Base Case: If we have processed all elements
            if idx == n:
                # Return 1 only if both sequences are non-empty (g1 > 0, g2 > 0)
                # and their final GCDs are equal.
                return 1 if (g1 > 0 and g1 == g2) else 0
            
            state = (idx, g1, g2)
            if state in memo:
                return memo[state]
            
            # Option 1: Skip the current element entirely
            res = solve(idx + 1, g1, g2)
            
            # Option 2: Add the current element to Sequence 1
            new_g1 = nums[idx] if g1 == 0 else gcd(g1, nums[idx])
            res = (res + solve(idx + 1, new_g1, g2)) % MOD
            
            # Option 3: Add the current element to Sequence 2
            new_g2 = nums[idx] if g2 == 0 else gcd(g2, nums[idx])
            res = (res + solve(idx + 1, g1, new_g2)) % MOD
            
            memo[state] = res
            return res

        return solve(0, 0, 0)

# ==========================================
# Example Trace: nums = [10, 20, 30]
# ------------------------------------------
# Some of the valid pairs counted:
# 1. seq1 formed by indices [0] (val: 10) -> GCD = 10
#    seq2 formed by indices [1, 2] (vals: 20, 30) -> GCD = gcd(20, 30) = 10
#    Since GCDs are equal (10 == 10), this is valid!
#
# 2. seq1 formed by indices [1, 2] (vals: 20, 30) -> GCD = 10
#    seq2 formed by indices [0] (val: 10) -> GCD = 10
#    Since sequences are disjoint, this is another unique pair!
# Total valid count for [10, 20, 30] is 2.
# ==========================================