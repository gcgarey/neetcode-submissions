class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = float('inf')
        while l <= r:
            mid = (l + r) // 2
            munch = 0
            for p in piles:
                munch += math.ceil(p/mid)
            if munch > h:
                l = mid + 1  
            elif munch <= h:
                r = mid - 1
                k = min(k, mid)
        return k


        