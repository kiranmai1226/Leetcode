from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_1 = defaultdict(int)
        out = set()
        for i in nums1:
            count_1[i] += 1
        for j in nums2:
            if (j in count_1):
                out.add(j)
        return list(out)
        