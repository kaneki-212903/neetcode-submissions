from collections import Counter
class Solution:
    def pair(self,s,t):
        return Counter(s)==Counter(t)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited=set()
        result=[]
        for i in range(len(strs)):
            if i in visited:
                continue
            ele=[strs[i]]
            visited.add(i)
            for j in range(i+1,len(strs)):
                if self.pair(strs[i],strs[j]):
                    ele.append(strs[j])
                    visited.add(j)
            result.append(ele)
        return result