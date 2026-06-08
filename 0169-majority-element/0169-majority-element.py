class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = sorted(nums)
        n = len(a)
        return a[n//2]