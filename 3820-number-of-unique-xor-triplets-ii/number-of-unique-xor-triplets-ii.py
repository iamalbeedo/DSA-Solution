class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Precompute all pairwise XOR combinations (a ^ b)
        pair_xors = {a ^ b for a in nums for b in nums}
        
        # Combine pair XORs with the 3rd element c
        triplet_xors = {ab ^ c for ab in pair_xors for c in nums}
        
        return len(triplet_xors)