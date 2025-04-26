from collections import defaultdict
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        my_dict={chr(i):i-96 for i in range(97,123)}
        result=0
        result2=0
        print(my_dict)
        input=''
        for i in s:
            input+=str(my_dict[i])
        input=int(input)
        while k>0:
            result=0
            while input>0:
                l=input%10
                result=result+l
                input=input//10
            k-=1
            input=result
            
        return result


      