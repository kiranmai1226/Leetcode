class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies=max(candies)
        boolean=[]
        for i in candies:
            boolean.append(i+extraCandies>=max_candies)
        return boolean
      
        