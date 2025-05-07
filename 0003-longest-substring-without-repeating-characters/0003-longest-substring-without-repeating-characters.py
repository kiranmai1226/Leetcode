from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=defaultdict(int)
        start=0
        result=0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>=start:
                start=seen[s[i]]+1
            seen[s[i]]=i
            result=max(result,i-start+1)
        return result
            