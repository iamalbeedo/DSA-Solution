class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            seen = set()
            for x in nums[i:]:  # grow the subarray to the right
                seen.add(x)  # a repeat doesn't change the size
                total += len(seen) ** 2
        return total