from collections import deque,defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list=defaultdict(list)
        for u,v in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        visited=set()
        q=deque([(0,-1)])
        visited.add(0)
        while q:
            node,par=q.popleft()
            for neighbour in adj_list[node]:
                if neighbour==par:
                    continue
                if neighbour in visited:
                    return False
                visited.add(neighbour)
                q.append((neighbour,node))
        return len(visited)==n
                