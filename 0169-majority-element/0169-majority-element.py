class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        return sorted(count, key = count.get, reverse = True)[0]
        