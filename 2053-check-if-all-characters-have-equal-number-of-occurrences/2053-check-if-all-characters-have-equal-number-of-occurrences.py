from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        seen=defaultdict(int)
        for i in range(len(s)):
            seen[s[i]]+=1
        for i in range(len(s)-1):
            if seen[s[i]]!=seen[s[i+1]]:
                return False
        return True
        