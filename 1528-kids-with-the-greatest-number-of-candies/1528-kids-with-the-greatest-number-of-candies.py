class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy=-65535
        for i in candies:
            max_candy=max(max_candy,i)
        boolean=[]
        for i in candies:
            boolean.append(i+extraCandies>=max_candy)
        return boolean
      
        