class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)+1
        n2=len(text2)+1
        dp=[[0]*n1 for _ in range(n2)]
        for i in range(1,n2):
            for j in range(1,n1):
                if text2[i-1]==text1[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n2-1][n1-1]