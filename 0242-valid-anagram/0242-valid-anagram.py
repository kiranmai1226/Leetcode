class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in s:
            count[i] += 1
        for i in t:
            if i in count:
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
        return count == {}