class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length=len(nums[0])
        binary=[]
        for i in range(2**length):
            binary.append(format(i,f'0{length}b'))

        for i in binary:
            if i not in nums:
                return i