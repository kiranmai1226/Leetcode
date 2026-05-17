class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            find = target - nums[i]
            if find in count:
                return [i, count[find]]
            count[nums[i]] = i
        return []
        