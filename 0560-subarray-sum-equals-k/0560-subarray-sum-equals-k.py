from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict=defaultdict(int)
        mydict[0]=1
        current_sum=0
        count=0
        for i,num in enumerate(nums):
            current_sum+=num
            count+=mydict[current_sum-k]
            mydict[current_sum]+=1
        return count
        