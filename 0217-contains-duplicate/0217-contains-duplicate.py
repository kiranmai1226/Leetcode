class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s= {}
        for i,num in enumerate(nums):
            if num in s:
                return True
            s[num] = i
        return False

        