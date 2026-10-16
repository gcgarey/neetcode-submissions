class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def buildDict(s):
            d = {}
            for c in s:
                d[c] = d.get(c, 0) + 1
            return d

        lenstring, lensub = len(s2), len(s1)
        if lensub > lenstring: return False
        dicts1 = buildDict(s1)
        dicts2 = buildDict(s2[:lensub])

        for i in range(0, lenstring-lensub):
            if dicts1 == dicts2: return True
            if dicts2[s2[i]] == 1:
                dicts2.pop(s2[i])
            else:
                dicts2[s2[i]] = dicts2[s2[i]] - 1
            dicts2[s2[i + lensub]] = dicts2.get(s2[i + lensub], 0) + 1
        return (dicts1 == dicts2)

        