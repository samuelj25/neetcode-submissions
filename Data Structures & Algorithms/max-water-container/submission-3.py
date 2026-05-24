class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0

        while l < r:
            dist = r - l
            height = min(heights[l], heights[r])
            curr = dist * height
            area = max(curr, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area
