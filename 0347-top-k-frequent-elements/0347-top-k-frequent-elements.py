class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            if nums[i] not in count:
                count[nums[i]] = 1
        sorte = sorted(count, key = count.get, reverse = True)
        return sorte[:k]