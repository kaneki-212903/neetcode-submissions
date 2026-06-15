class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        one=1
        two=1
        for i in range(2,len(s)+1):
            current=0
            if 0<int(s[i-1:i])<=9:
                current+=one
            if 10<=int(s[i-2:i])<=26:
                current+=two
            two,one=one,current
        return one
