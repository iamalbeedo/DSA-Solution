class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Optimize shift count by removing full cycle wraps
        k %= total
        
        # Allocate output grid with initial placeholder values
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Map 2D coordinates (i, j) to a 1D linear index
                old_1d = i * n + j
                
                # Calculate new 1D index after shifting k positions right
                new_1d = (old_1d + k) % total
                
                # Unpack 1D index back to target 2D row and column
                new_row = new_1d // n
                new_col = new_1d % n
                
                result[new_row][new_col] = grid[i][j]
                
        return result