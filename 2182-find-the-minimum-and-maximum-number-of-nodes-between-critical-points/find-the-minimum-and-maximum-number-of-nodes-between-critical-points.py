# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        index = 1

        first_critical = -1
        prev_critical = -1
        min_distance = float('inf')

        while curr.next:
            nxt = curr.next

            # Check if current node is a critical point
            is_local_maxima = curr.val > prev.val and curr.val > nxt.val
            is_local_minima = curr.val < prev.val and curr.val < nxt.val

            if is_local_maxima or is_local_minima:
                if first_critical == -1:
                    first_critical = index
                else:
                    min_distance = min(min_distance, index - prev_critical)
                prev_critical = index

            prev = curr
            curr = nxt
            index += 1

        # Return [-1, -1] if fewer than two critical points are found
        if first_critical == -1 or prev_critical == first_critical:
            return [-1, -1]

        max_distance = prev_critical - first_critical
        return [min_distance, max_distance]