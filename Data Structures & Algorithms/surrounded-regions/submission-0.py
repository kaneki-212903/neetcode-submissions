from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited= set()
        q=deque()
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if board[i][j]=="O":
                        visited.add((i,j))
                        q.append((i,j))
        while q:
            r,c=q.popleft()
            board[r][c]="r"
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr=dr+r
                nc=dc+c
                if 0<=nr<m and 0<=nc<n:
                    if (nr,nc) not in visited:
                        if board[nr][nc]=="O":
                            q.append((nr,nc))
                            visited.add((nr,nc))
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="r":
                    board[i][j]="O"
        return