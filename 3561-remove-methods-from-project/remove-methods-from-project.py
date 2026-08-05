from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Step 1: Build graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Step 2: Find all suspicious nodes via BFS
        is_suspicious = [False] * n
        queue = deque([k])
        is_suspicious[k] = True

        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if not is_suspicious[neighbor]:
                    is_suspicious[neighbor] = True
                    queue.append(neighbor)

        # Step 3: Check for external invocations into suspicious nodes
        for u, v in invocations:
            if not is_suspicious[u] and is_suspicious[v]:
                return list(range(n))

        # Step 4: Return non-suspicious nodes
        return [i for i in range(n) if not is_suspicious[i]]