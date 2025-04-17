from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict={}
        for i,num in enumerate(nums):
            difference=target-num
            if difference in mydict:
                return [mydict[difference],i]
            mydict[num]=i
        return [] 