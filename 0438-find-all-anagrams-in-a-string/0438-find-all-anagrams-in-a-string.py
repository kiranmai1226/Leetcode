from collections import defaultdict 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = defaultdict(int)
        match = defaultdict(int)
        output = []
        for i in p:
            count[i] += 1
        left = 0
        for right in range(len(s)):
            match[s[right]] += 1
            if right - left + 1 > len(p):
                match[s[left]] -= 1
                if match[s[left]] == 0:
                    del match[s[left]]
                left += 1
            if match == count:
                output.append(left)
        return output