class Solution:
    def isRectangleOverlap(self, r1: List[int], r2: List[int]) -> bool:
        return r1[0]<r2[2] and r2[0]<r1[2] and r1[1]<r2[3] and r2[1]<r1[3]