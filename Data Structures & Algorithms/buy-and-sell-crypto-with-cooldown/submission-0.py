class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        held=[0]*n
        reset=[0]*n
        sold=[0]*n
        held[0]=-prices[0]
        for i in range(1,n):
            held[i]=max(held[i-1],reset[i-1]-prices[i])
            sold[i]=held[i-1]+prices[i]
            reset[i]=max(reset[i-1],sold[i-1])
        return max(sold[n-1],reset[n-1])