from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        mydict=defaultdict(int)
        for i in nums:
            mydict[i]+=1
            if mydict[i]>n//2:
                return i