from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Line 1: Build an adjacency list to record graph connections.
        adj = [[] for _ in range(n)]
        
        # Line 2: Create an array to keep track of the number of edges (degree) attached to each node.
        degree = [0] * n
        
        # Line 3: Fill the adjacency list and increment degrees for both nodes because it's undirected.
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        # Line 4: Set up a tracking mechanism to remember which nodes have been explored.
        visited = [False] * n
        complete_components_count = 0
        
        # Line 5: Iterate through every node in the graph.
        for i in range(n):
            if not visited[i]:
                # Collect all nodes belonging to the current connected component.
                component_nodes = []
                
                # Standard BFS configuration using a double-ended queue.
                queue = deque([i])
                visited[i] = True
                
                while queue:
                    curr = queue.popleft()
                    component_nodes.append(curr)
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            
                # Line 6: Check if the discovered component is complete.
                total_nodes = len(component_nodes)
                is_complete = True
                
                # Every node in a complete graph must connect to all other nodes in its group.
                for node in component_nodes:
                    if degree[node] != total_nodes - 1:
                        is_complete = False
                        break
                        
                if is_complete:
                    complete_components_count += 1
                    
        # Line 7: Return the absolute total of perfect components.
        return complete_components_count