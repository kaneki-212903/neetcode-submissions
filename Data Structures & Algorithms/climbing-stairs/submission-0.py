class Solution:
    def climbStairs(self, n: int) -> int:
        memory={}
        def ways(i):
            if i==1:
                return 1
            if i==2:
                return 2
            if i in memory:
                return memory[i]
            memory[i]=ways(i-1)+ways(i-2)
            return memory[i]
        return ways(n)