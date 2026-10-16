class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we know the bounds of our search will be the smallest 
        # and largest numbers in piles (h >= max(piles))

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res