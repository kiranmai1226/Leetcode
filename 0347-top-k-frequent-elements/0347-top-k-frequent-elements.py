class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        for i in nums:
            a[i] += 1
        r = list(sorted(a, key = a.get, reverse =True))
        return r[:k]
        