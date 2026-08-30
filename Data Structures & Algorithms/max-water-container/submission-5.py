class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while (l < r):
            dist = r - l
            res = max(res, dist * min(heights[l], heights[r]))
            
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        
        return res
