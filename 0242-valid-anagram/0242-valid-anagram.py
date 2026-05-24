class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0]*26
        for i in range(len(s)):
            if s[i] not in arr:
                arr[ord(s[i]) - ord('a')] += 1
            if t[i] not in arr:
                arr[ord(t[i]) - ord('a')] -= 1
        if not any(arr):
            return True
        else:
            return False