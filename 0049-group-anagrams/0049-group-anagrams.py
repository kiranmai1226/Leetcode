class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            s = ''.join(sorted(word))
            count[s].append(word)
        return list(count.values())
        