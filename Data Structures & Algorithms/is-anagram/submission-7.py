class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

        for c in s:
            h[c] = h.get(c, 0) + 1
        
        for c in t:
            if c not in h:
                return False

            h[c] = h.get(c, 0) - 1            
            if h[c] == 0:
                del h[c]
        
        return len(h) == 0
