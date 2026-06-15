class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        def rob_helper(arr):
            n=len(arr)
            dp=[0]*n
            dp[0]=arr[0]
            
            dp[1]=max(arr[0],arr[1])
            for i in range(2,n):
                dp[i]=max(dp[i-2]+arr[i],dp[i-1])
            return dp[n-1]
        path1=rob_helper(nums[:-1])
        path2=rob_helper(nums[1:])
        print(path1,path2)
        return max(path1,path2)