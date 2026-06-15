class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        maxi=0
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[right]==s[left]:
                if (right-left+1)>maxi:
                    maxi=right-left+1
                    res=s[left:right+1]
                left-=1
                right+=1
            
            left,right=i,i+1
            while left>=0 and right<len(s) and s[right]==s[left]:
                if (right-left+1)>maxi:
                    maxi=right-left+1
                    res=s[left:right+1]
                left-=1
                right+=1
        return res