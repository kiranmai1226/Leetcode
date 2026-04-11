class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        S = {}
        for i,num in enumerate(nums):
            if num in S:
                return True
            S[num] = i
        return False

        