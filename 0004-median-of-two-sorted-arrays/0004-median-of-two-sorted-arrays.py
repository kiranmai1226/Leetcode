class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list3=sorted(nums1+nums2)
        if len(list3)%2==0:
            middle=len(list3)//2
            print(middle)
            return (list3[middle-1]+list3[middle])/2
        else:
            middle=len(list3)//2
            return list3[middle]