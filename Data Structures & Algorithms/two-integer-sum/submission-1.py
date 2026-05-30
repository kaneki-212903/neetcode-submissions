class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums=[[a,b] for (a,b) in enumerate(nums)]
        sorted_nums=sorted(new_nums,key=lambda x:x[1])
        i,j=0,len(nums)-1
        while i<j:
            temp=sorted_nums[i][1]+sorted_nums[j][1]
            if temp>target:
                j-=1
            elif temp<target:
                i+=1
            else:
                return sorted([sorted_nums[i][0],sorted_nums[j][0]])
