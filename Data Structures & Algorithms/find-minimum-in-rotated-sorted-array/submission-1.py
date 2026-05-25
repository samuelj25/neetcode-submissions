class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = min(nums[0], nums[-1])

        while (l <= r):
            mid = (r + l) // 2
            
            if (nums[mid] > res):
                l = mid + 1
            else:
                r = mid - 1
            
            res = min(res, nums[mid])
        
        return res
            
