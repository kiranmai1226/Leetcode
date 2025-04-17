from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict=defaultdict(int)
        for i in s:
            mydict[i]+=1
        for key,values in mydict.items():
            if values==1:
                return s.index(key)
        return -1
        