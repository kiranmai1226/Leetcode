from collections import defaultdict
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums=''.join(str(ord(i)-96) for i in s)
        for _ in range(k):
            nums=str(sum(int(num) for num in nums))
        return int(nums)

      