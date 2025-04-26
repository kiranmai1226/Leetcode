class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        concat=''.join(str(i) for i in words)
        k=0
        for i in words:

            j=len(i)
            if i!=s[k:k+j]:
                return False
            k+=j
            if k==len(s):
                return True
        return False
        