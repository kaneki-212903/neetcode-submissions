class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        dp=[[1]*m for _ in range(n)]
        dp[0][0]=0
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]