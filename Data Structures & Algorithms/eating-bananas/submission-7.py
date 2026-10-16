class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = -1

        while l <= r:
            total = 0
            k = (l + r) // 2
            for p in piles:
                total += math.ceil(p / k)
            if total <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res
1
        
        