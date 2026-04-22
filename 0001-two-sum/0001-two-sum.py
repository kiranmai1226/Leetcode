class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      Sum = {}
      for i,num in enumerate(nums):
        temp = target - num
        if num in Sum:
            return [i, Sum[num]]
        Sum[temp] = i
    
