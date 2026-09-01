from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_x, start_y = -1, -1
        litters = []
        
        # Locate the starting point 'S' and all litter items 'L'
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_x, start_y = i, j
                elif classroom[i][j] == 'L':
                    litters.append((i, j))
                    
        num_litters = len(litters)
        full_mask = (1 << num_litters) - 1
        
        # Map each litter position to a unique bit index
        litter_map = {pos: idx for idx, pos in enumerate(litters)}
        
        # Track maximum remaining energy recorded for state (x, y, mask)
        best_energy = {}
        
        # Set up initial state mask if starting position contains litter
        initial_mask = 0
        if (start_x, start_y) in litter_map:
            initial_mask |= (1 << litter_map[(start_x, start_y)])
            
        queue = deque([(start_x, start_y, initial_mask, energy)])
        best_energy[(start_x, start_y, initial_mask)] = energy
        
        steps = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            for _ in range(len(queue)):
                x, y, mask, rem_energy = queue.popleft()
                
                # Target state: all litter collected
                if mask == full_mask:
                    return steps
                
                # If energy reached 0 and we are NOT on a reset cell 'R', cannot step further
                if rem_energy == 0 and classroom[x][y] != 'R':
                    continue
                
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    
                    # Boundary check and obstacle check
                    if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                        next_energy = rem_energy - 1
                        cell = classroom[nx][ny]
                        
                        # Reset energy if entering reset cell 'R'
                        if cell == 'R':
                            next_energy = energy
                            
                        next_mask = mask
                        if (nx, ny) in litter_map:
                            next_mask |= (1 << litter_map[(nx, ny)])
                            
                        # Only push state to queue if we achieve higher remaining energy
                        if next_energy > best_energy.get((nx, ny, next_mask), -1):
                            best_energy[(nx, ny, next_mask)] = next_energy
                            queue.append((nx, ny, next_mask, next_energy))
            steps += 1
            
        return -1