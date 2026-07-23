class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # Bit length of n gives the number of bits needed (MSB + 1)
        # 1 << n.bit_length() computes 2^(bit_length)
        return 1 << n.bit_length()