class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def Palindrome(left:int, right:int)-> str:
            while left >=0 and right < n and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        longest=''
        for i in range(n):
            p1=Palindrome(i,i)
            p2=Palindrome(i,i+1)
            if len(p1)>len(longest):
                longest=p1
            if len(p2)>len(longest):
                longest=p2
        return longest