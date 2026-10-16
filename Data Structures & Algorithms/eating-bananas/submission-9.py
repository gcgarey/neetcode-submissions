class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pile[i] * total / h
        res = 10000000000
        l, r = 1, max(piles)
        while l <= r:
            rate = (l + r) // 2
            total = 0

            for pile in piles:
                total += math.ceil(pile / rate)
            
            if total <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1

        return res
        