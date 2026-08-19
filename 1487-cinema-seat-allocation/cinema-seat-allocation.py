from collections import defaultdict
from typing import List


class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reserved_rows = defaultdict(int)

        for row, seat in reservedSeats:
           
            reserved_rows[row] |= 1 << seat

        total_groups = (n - len(reserved_rows)) * 2

        left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)  # Seats 2, 3, 4, 5
        right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)  # Seats 6, 7, 8, 9
        middle_mask = (
            1 << 4
        ) | (
            1 << 5
        ) | (
            1 << 6
        ) | (
            1 << 7
        )

        for mask in reserved_rows.values():
            left_available = (mask & left_mask) == 0
            right_available = (mask & right_mask) == 0
            middle_available = (mask & middle_mask) == 0

            if left_available and right_available:
                total_groups += 2
            elif left_available or right_available or middle_available:
                total_groups += 1

        return total_groups