import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        S = re.sub(r'[^a-z0-9]',"",s)
        return S == S[::-1]
        