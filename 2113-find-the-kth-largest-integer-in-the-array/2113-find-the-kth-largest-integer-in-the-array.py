class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_1=[]
        for i in nums:
            nums_1.append(int(i))
        nums_2=sorted(nums_1)
        print(nums_2)
        return str(nums_2[-k])
        