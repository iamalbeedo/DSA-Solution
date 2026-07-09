class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # WHAT: Create a list to track the component group identifier for each node index.
        # WHY: Allows us to remember which block of continuous numbers a node belongs to.
        component_id = [0] * n
        current_component = 0
        
        # WHAT: Linear sweep to compute component groups.
        # WHY: Since the array is sorted, any difference > maxDiff partitions the graph.
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                current_component += 1
            component_id[i] = current_component
            
        # WHAT: Process queries via a list comprehension in O(1) per lookup.
        # WHY: Avoids nested loop overhead, verifying component matches instantly.
        return [component_id[u] == component_id[v] for u, v in queries]