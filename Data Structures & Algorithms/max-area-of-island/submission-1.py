class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ## do again 
        area = 0 
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # 1. Fixed typo 'gird' -> 'grid'
            # 2. Fixed string "0" -> integer 0
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            # Mark as visited by setting to 0
            grid[r][c] = 0

            # 3. Accumulate area for the current cell (1) plus all 4 directions
            current_area = 1
            for dr, dc in directions:
                current_area += dfs(r + dr, c + dc)
            
            return current_area
        
        for i in range(ROWS):
            for j in range(COLS):
                # Fixed string "1" -> integer 1
                if grid[i][j] == 1:
                    a = dfs(i, j)
                    # 4. Removed the '1 +' to prevent double-counting
                    area = max(area, a)
                    
        return area