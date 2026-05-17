from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_1 = defaultdict(int)
        out = []
        for i in max(nums1,nums2):
            count_1[i] += 1
        for j in min(nums1,nums2):
            if (j in count_1):
                del count_1[j]
                out.append(j)
        return out
        