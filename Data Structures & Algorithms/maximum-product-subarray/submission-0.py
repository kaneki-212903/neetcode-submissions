class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        maxi=nums[0]
        mini=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            curr=nums[i]
            if curr<0:
                maxi,mini=mini,maxi
            maxi=max(curr,maxi*curr)
            mini=min(curr,mini*curr)
            res=max(res,maxi)
        return res