from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        m,n=len(grid[0]),len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
        res=0
        while q:
            r,c,mi=q.popleft()
            res=mi
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m:
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc,mi+1))
        for a in range(n):
            for b in range(m):
                if grid[a][b]==1:
                    return -1
        return res
