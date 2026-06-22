from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q=deque()
        adj=defaultdict(list)
        topo=[]
        indegree=[0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            curr=q.popleft()
            topo.append(curr)
            for nei in adj[curr]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(topo)!=numCourses:
            return False
        return True
                    
                
