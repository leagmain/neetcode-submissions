class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            ss = ''.join(sorted(s))
            h[ss] = h.get(ss, [])
            h[ss].append(s)
        return list(h.values())