class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        word3=""
        min_index=min(a,b)
        for i in range(min_index):
            word3=word3+word1[i]+word2[i]
        if a<b:    
            return word3+word2[min_index:]
        elif b<a:
            return word3+word1[min_index:]
        else:
            return word3

        