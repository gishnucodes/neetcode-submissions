class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0:
                    queue.append((r,c))
        
        
        
        while queue:

            r,c = queue.popleft()
            
            for dr, dc in directions:
                
                if r+dr < 0 or r+dr >= ROWS or c+dc < 0 or c+dc >=COLS or grid[r+dr][c+dc]!=2147483647:
                    continue 
                grid[r+dr][c+dc]=grid[r][c]+1
                queue.append((r+dr,c+dc))
            
        



                


