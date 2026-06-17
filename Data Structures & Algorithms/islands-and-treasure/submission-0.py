from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q=deque()
        m,n=len(grid[0]),len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            r,c=q.popleft()
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m:
                    if grid[nr][nc]==2147483647:
                        grid[nr][nc]=grid[r][c]+1
                        q.append((nr,nc))
                            
        
        return 
    
        
                

        

          