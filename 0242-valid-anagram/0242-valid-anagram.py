from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict1=defaultdict(int)
        mydict2=defaultdict(int)
        for i in s:
            mydict1[i]+=1
        for i in t:
            mydict2[i]+=1
        return mydict1==mydict2