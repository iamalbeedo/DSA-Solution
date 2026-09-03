class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        odds = [x for x in nums1 if x % 2 != 0]
        min_odd = min(odds) if odds else float('inf')

        if min_val % 2 != 0:
            return True

        can_be_even = True
        for num in nums1:
            if num % 2 != 0 and num <= min_odd:
                can_be_even = False
                break

        can_be_odd = True
        for num in nums1:
            if num % 2 == 0 and num <= min_odd:
                can_be_odd = False
                break

        return can_be_even or can_be_odd