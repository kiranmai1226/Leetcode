class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        result=0
        i=0
        while i<(len(s)-1):
            if s[i]+s[i+1] in my_dict:
                result+=my_dict[s[i]+s[i+1]]
                i+=1
            else:
                result+=my_dict[s[i]]
            i+=1
        if i==len(s)-1:
            result+=my_dict[s[i]]
        return result
        