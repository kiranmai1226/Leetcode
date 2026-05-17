from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_1 = defaultdict(int)
        out = []
        for i in nums1:
            count_1[i] += 1
        for j in nums2:
            if (j in count_1) and (j not in out):
                out.append(j)
        return out
        