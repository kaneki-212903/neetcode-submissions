class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi=0
        n=len(s)
        if n==1:
            return s
        if n==2:
            if s==s[::-1]:
                return s
            else:
                return s[0]
        res=''
        for i in range(1,n+1):
            for j in range(0,i):
                curr=s[j:i]
                if curr==curr[::-1]:
                    if len(curr)>maxi:
                        res=curr
                        maxi=len(curr)
                else:
                    continue
        return res