class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sort = sorted(nums)
        n = len(nums)
        return sort[n//2]