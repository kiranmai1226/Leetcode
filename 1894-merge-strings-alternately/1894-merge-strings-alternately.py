class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        word3=[]
        i=0
        j=0
        while i<a and j<b:
            word3.append(word1[i])
            word3.append(word2[j])
            i+=1
            j+=1
        word3.append(word1[i:])
        word3.append(word2[j:])
        return "".join(word3)


        