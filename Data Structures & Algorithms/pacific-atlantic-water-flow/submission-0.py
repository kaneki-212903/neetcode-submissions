from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m,n=len(heights),len(heights[0])

        pacific_visited=set()
        atlantic_visited=set()
        
        #Pacific
        pacific_q=deque()
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    pacific_q.append((i,j))
                    pacific_visited.add((i,j))
        while pacific_q:
            r,c=pacific_q.popleft()
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n:
                    if (nr,nc) not in pacific_visited:
                        if heights[nr][nc]>=heights[r][c]:
                            pacific_visited.add((nr,nc))
                            pacific_q.append((nr,nc))
        #Atlantic
        atlantic_q=deque()
        for i in range(m):
            for j in range(n):
                if i==m-1 or j==n-1:
                    atlantic_visited.add((i,j))
                    atlantic_q.append((i,j))
        while atlantic_q:
            r,c=atlantic_q.popleft()
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n:
                    if (nr,nc) not in atlantic_visited:
                        if heights[nr][nc]>=heights[r][c]:
                            atlantic_q.append((nr,nc))
                            atlantic_visited.add((nr,nc))
        res=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific_visited and (i,j) in atlantic_visited:
                    res.append([i,j])
        return res
        