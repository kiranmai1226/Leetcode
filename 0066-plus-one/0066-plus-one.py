class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=int(''.join(map(str,digits)))
        j=s+1
        j=str(j)
        result=list(map(int,j))
        return result
            



            