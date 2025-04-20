from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count=0
        subarray_sum=0
        my_dict=defaultdict(int)
        my_dict[0]=1
        for num in nums:
            subarray_sum+=num
            count+=my_dict[subarray_sum-k]
            my_dict[subarray_sum]+=1

        return count

       