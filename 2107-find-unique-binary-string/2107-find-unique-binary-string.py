class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length=len(nums[0])
        binary=[]
        for i in range(2**length):
            if format(i,f'0{length}b') not in nums:
                return format(i,f'0{length}b')