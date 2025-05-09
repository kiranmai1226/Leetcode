class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        prefix_product=1
        suffix_product=1
        for i in range(len(nums)):
            result[i]=prefix_product
            prefix_product*=nums[i]
        for i in range(n-1,-1,-1):
            result[i]*=suffix_product
            suffix_product*=nums[i]
        return result


        