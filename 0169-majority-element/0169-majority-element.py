from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current=0
        count=0
        for i in nums:
            if count==0:
                current=i
            count+=(1 if i==current else -1)
        return current