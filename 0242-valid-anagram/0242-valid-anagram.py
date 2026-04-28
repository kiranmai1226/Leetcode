class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i,num in enumerate(s):
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for i,char in enumerate(t):
            if char not in count:
                return False
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        if not count:
            return True

        