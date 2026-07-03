from collections import defaultdict
import heapq

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        
        # WHAT: Build an adjacency list to represent our Directed Graph.
        # WHY: It allows efficient O(1) lookups of adjacent neighbors during graph traversal.
        adj = defaultdict(list)
        max_cost = 0
        
        for u, v, cost in edges:
            # WHAT: Only add edges where the destination node 'v' is online (or is the destination n-1).
            # WHY: If a network node is offline, no valid recovery path can pass through it. Skipping it saves overhead.
            if online[v]:
                adj[u].append((v, cost))
                max_cost = max(max_cost, cost)
                
        # WHAT: Initialize Binary Search boundaries.
        # WHY: The optimum path score must lie between 0 and the maximum edge cost present in the network.
        low, high = 0, max_cost
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # WHAT: Check if a path exists where every edge has a cost >= mid and total path cost <= k.
            # WHY: If it's valid, we aggressively search the right half to see if we can get an even larger minimum edge cost.
            if self.is_valid(n, adj, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans

    def is_valid(self, n: int, adj: dict, k: int, min_edge_cost: int) -> bool:
        # WHAT: Min-Heap for Dijkstra's algorithm storing pairs of (accumulated_cost, node).
        # WHY: Dijkstra greedily expands paths with the absolute lowest cumulative cost to find the optimal path to n-1.
        pq = [(0, 0)]  # (cost, node)
        
        # WHAT: Create a tracking dictionary initialized to infinity.
        # WHY: We keep track of the minimum cost to reach each node to avoid re-evaluating sub-optimal routes.
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        
        while pq:
            current_cost, u = heapq.heappop(pq)
            
            # WHAT: Early exit check when reaching the target destination node.
            # WHY: Because it's a min-heap, the first time node n-1 is popped, it is guaranteed to hold the lowest cumulative cost.
            if u == n - 1:
                return current_cost <= k
                
            # WHAT: Optimization skip.
            # WHY: If we already discovered a cheaper alternative to reach node 'u', discard this stale heap entry.
            if current_cost > min_cost[u]:
                continue
                
            for v, edge_cost in adj[u]:
                # WHAT: Filter out edges below our Binary Search threshold.
                # WHY: We completely ignore edges that don't satisfy the minimum edge cost requirement.
                if edge_cost >= min_edge_cost:
                    next_cost = current_cost + edge_cost
                    
                    # WHAT: Relaxation step if a cheaper path to node 'v' is discovered.
                    # WHY: We only push to our heap if the path satisfies our budget constraint 'k' and is strictly cheaper.
                    if next_cost <= k and next_cost < min_cost[v]:
                        min_cost[v] = next_cost
                        heapq.heappush(pq, (next_cost, v))
                        
        return False