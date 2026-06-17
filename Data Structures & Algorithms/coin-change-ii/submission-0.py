class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memory={}
        def ways(i,remain):
            if remain==0:
                return 1
            if remain<0:
                return 0
            if i>=len(coins):
                return 0
            if (i,remain) in memory:
                return memory[(i,remain)]
            memory[(i,remain)]=ways(i+1,remain)+ways(i,remain-coins[i])
            return memory[(i,remain)]
        return ways(0,amount)