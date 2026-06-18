from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=defaultdict(list)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            adj_list[v].append(u)
            indegree[u]+=1
        q=deque([i for i in range(numCourses) if indegree[i]==0])
        topo=[]
        while q:
            curr=q.popleft()
            topo.append(curr)
            
            for neighbour in adj_list[curr]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        if len(topo)!=numCourses:
            return []
        return topo