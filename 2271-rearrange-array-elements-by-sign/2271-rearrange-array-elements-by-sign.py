class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        temp=[0]*len(nums)
        for k in range(len(nums)):
            if nums[k]>0:
                temp[i]=nums[k]
                i+=2
            else:
                temp[j]=nums[k]
                j+=2
        nums=temp
        return nums
        