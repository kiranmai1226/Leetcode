class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=[]
        s=''
        for i in digits:
            s=s+str(i)
        s=int(s)
        j=s+1
        j=str(j)
        for i in j:
            result.append(int(i))
        return result
            



            