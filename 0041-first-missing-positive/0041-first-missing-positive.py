class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        prevous=0
        after=0
        idx=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[idx]=nums[i]
                idx+=1
        nums=nums[:idx]
        if 1 not in nums:
            return 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]!=1 :
                return nums[i]+1
        return nums[-1]+1
