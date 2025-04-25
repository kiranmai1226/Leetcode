from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        seen=defaultdict(int)
        for i in range(len(s)):
            seen[s[i]]+=1
        
        return len(set(seen.values()))==1