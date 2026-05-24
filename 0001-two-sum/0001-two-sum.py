class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count  = defaultdict()
        for i in range(len(nums)):
            find  = target - nums[i]
            if find in count:
                return [count[find],i]
            count[nums[i]] = i
        