from collections import Counter
class Solution:
    def pair(self,s,t):
        return Counter(s)==Counter(t)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        for s in strs:
            key="".join(sorted(s))
            if key not in hash:
                hash[key]=[]
            hash[key].append(s)
        return list(hash.values())