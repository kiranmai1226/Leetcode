class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in strs:
            collect = "".join(sorted(i))
            count[collect].append(i)
        return list(count.values())