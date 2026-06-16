from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        for a in nums:
            total+=a
        if total%2!=0:
            return False
        @cache
        def ways(i,remain):
            if remain==0:
                return True
            if remain<0:
                return False
            if i>=len(nums):
                return False
            return ways(i+1,remain-nums[i]) or ways(i+1,remain)
        return ways(0,total//2)
