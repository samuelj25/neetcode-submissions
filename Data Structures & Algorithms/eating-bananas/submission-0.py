class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while (l <= r):
            curr_k = (l + r) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / curr_k)
            
            if (time <= h):
                k = min(k, curr_k)
                r = curr_k - 1
            else:
                l = curr_k + 1
        
        return k