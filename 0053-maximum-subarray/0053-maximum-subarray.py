class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-65535
        sum_1=0
        for i in nums:
            sum_1+=i
            maxi=max(sum_1,maxi)
            if sum_1<0:
                sum_1=0
        return maxi
            

            
        