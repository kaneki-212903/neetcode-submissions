from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        distances={i:float('inf') for i in range(1,n+1)}
        distances[k]=0
        minheap=[(0.0,k)]
        visit=set()
        while minheap:
            curr_cost,node=heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            for nei,weight in adj[node]:
                if nei in visit:
                    continue
                new_cost=curr_cost+weight
                if new_cost<distances[nei]:
                    distances[nei]=new_cost
                    heapq.heappush(minheap,(new_cost,nei))
        maxtime= max(distances.values())
        return int(maxtime) if maxtime<float('inf') else -1