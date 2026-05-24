class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        curr_sum = 0
        result = 0
        for i in nums:
            curr_sum += i
            result += count[curr_sum - k]
            count[curr_sum] += 1
        return result