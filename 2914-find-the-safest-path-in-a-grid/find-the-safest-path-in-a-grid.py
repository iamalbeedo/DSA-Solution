from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # Step 1: Multi-source BFS to find Manhattan distance to any thief
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque([(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1])
        
        for r, c in queue:
            dist[r][c] = 0

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # Step 2: Modified Dijkstra using a Max-Heap to find the safest path
        max_heap = [(-dist[0][0], 0, 0)]  # (negative safeness, row, col)
        visited = {(0, 0)}

        while max_heap:
            sf, r, c = heapq.heappop(max_heap)
            
            if r == n - 1 and c == n - 1:
                return -sf

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # Safeness of a path is limited by the minimum safeness value along its cells
                    heapq.heappush(max_heap, (max(sf, -dist[nr][nc]), nr, nc))

        return 0