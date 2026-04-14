class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= {}
        for i, num in enumerate(nums):
            temp = target-num
            if num in s:
                return [i,s[num]]
            s[temp] = i


                 