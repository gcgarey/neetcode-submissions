class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check edge case
        if len(s1) > len(s2):
            return False

        # make 2 hashmaps for s1 and s2 and populate
        s1map = defaultdict(int)
        s2map = defaultdict(int)

        for i in range(len(s1)):
            s1map[s1[i]] += 1
            s2map[s2[i]] += 1

        if s1map == s2map:
            return True

        # define a window of len(s1)
        l = 0
        # iterate through s2, slide window, check match
        for r in range(len(s1), len(s2)):
            s2map[s2[r]] += 1
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                del s2map[s2[l]]
            l += 1

            if s2map == s1map:
                return True
        return False


        