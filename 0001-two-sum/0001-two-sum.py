class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] = i
        for i in range(len(nums)):
            find = target - nums[i]
            if find in count and i != count[find]:
                return [i, count[find]]
        return []
        