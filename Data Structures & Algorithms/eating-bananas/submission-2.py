class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while (l <= r):
            mid = l + (r - l) // 2
            time = 0

            for p in piles:
                time += int(p // mid)
                time += 1 if p % mid != 0 else 0
                
            if (time <= h):
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return k
