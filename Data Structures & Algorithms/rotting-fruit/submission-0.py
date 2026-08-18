class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # find the rotten ones first and then do multi source BFS 

        q = deque()
        fresh = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
                
        while q and fresh > 0 :

            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if (0 <= nr < ROWS and 0<= nc < COLS and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
            time += 1 

        return time if fresh == 0 else -1 
        

            
        

