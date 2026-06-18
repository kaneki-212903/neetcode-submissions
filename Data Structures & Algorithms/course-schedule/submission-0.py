from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=defaultdict(list)
        indeg=[0]*numCourses
        for u,v in prerequisites:
            adj_list[v].append(u)
            indeg[u]+=1
        
        queue=deque([i for i in range(numCourses) if indeg[i]==0])
        topo=[]
        while queue:
            curr=queue.popleft()
            topo.append(curr)
            for neighbour in adj_list[curr]:
                indeg[neighbour]-=1
                if indeg[neighbour]==0:
                    queue.append(neighbour)
        if len(topo)!=numCourses:
            return False
        return True