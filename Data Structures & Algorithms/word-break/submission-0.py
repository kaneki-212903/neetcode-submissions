class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)+1
        dp=[False]*n
        dp[0]=True
        for i in range(1,n):
            for j in range(0,i):
                if dp[j]==True:
                    if s[j:i] in wordDict:
                        dp[i]=True
                else:
                    continue
        return dp[n-1]