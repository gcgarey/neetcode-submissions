class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check edge case
        if len(s1) > len(s2):
            return False

        # define hash maps to count freq
        s1count = defaultdict(int)
        s2count = defaultdict(int)

        # compare elements from s1
        for i in range(len(s1)):
            s1count[s1[i]] += 1
            s2count[s2[i]] += 1

        if s1count == s2count:
            return True

        # iterate from 3 -> 
        l = 0
        for r in range(len(s1), len(s2)):
            s2count[s2[r]] += 1
            s2count[s2[l]] -= 1 
            
            if s2count[s2[l]] == 0:
                del s2count[s2[l]]
            
            l += 1

            if s2count == s1count:
                return True

        return False

