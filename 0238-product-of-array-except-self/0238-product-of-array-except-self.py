class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        product = [1]*len(nums)
        temp = 1
        temp2 = 1
        for i in range(1,len(nums),1):
            temp = temp * nums[i-1]
            prefix[i] = temp
        for j in range(len(nums)-1,0,-1):
            temp2 = nums[j] * temp2
            suffix[j-1] = temp2
        print(prefix)
        print(suffix)
        for i in range(len(nums)):
            product[i] = prefix[i] * suffix[i]
        return product