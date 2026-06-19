from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list=defaultdict(list)
        n=len(edges)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visit=[False]*(n+1)
        cycle=set()
        cyclestart=-1
        def dfs(node,par):
            nonlocal cyclestart
            if visit[node]:
                cyclestart=node
                return True
            visit[node]=True
            for nei in adj_list[node]:
                if nei==par:
                    continue
                if dfs(nei,node):
                    if cyclestart!=-1:
                        cycle.add(node)
                    if node==cyclestart:
                        cyclestart=-1
                    return True
            return False
        
        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        



