class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = defaultdict(int)
        tmap = defaultdict(int)

        for ch in s:
            smap[ch] += 1
        
        for ch in t:
            tmap[ch] += 1

        return tmap == smap

        