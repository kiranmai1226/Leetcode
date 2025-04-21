from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict=defaultdict(int)
        for i,num in enumerate(nums):
            
            difference=target-num
            if difference in my_dict:
                return [i,my_dict[difference]]
            my_dict[num]=i