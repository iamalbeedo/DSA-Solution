from collections import defaultdict
from typing import List


class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Group reserved seats by row using a bitmask for each row
        reserved_rows = defaultdict(int)

        for row, seat in reservedSeats:
            # Set the seat-th bit to 1 to indicate it is reserved
            reserved_rows[row] |= 1 << seat

        # Calculate groups for completely empty rows upfront (each fits 2 groups)
        total_groups = (n - len(reserved_rows)) * 2

        # Define bitmasks for the three possible 4-person seating blocks
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
        )  # Seats 4, 5, 6, 7

        # Iterate through rows that have reservations
        for mask in reserved_rows.values():
            # A block is available if none of its bits overlap with reserved bits
            left_available = (mask & left_mask) == 0
            right_available = (mask & right_mask) == 0
            middle_available = (mask & middle_mask) == 0

            # Prioritize placing 2 groups (both left and right blocks)
            if left_available and right_available:
                total_groups += 2
            # Otherwise, place 1 group if any of the three blocks is completely free
            elif left_available or right_available or middle_available:
                total_groups += 1

        return total_groups