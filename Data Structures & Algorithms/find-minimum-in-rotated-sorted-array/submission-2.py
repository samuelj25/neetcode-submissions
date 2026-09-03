class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = min(nums[l], nums[r])

        while (l <= r):
            mid = l + (r - l) // 2

            if (nums[mid] < res):
                r = mid - 1
            else:
                l = mid + 1
            
            res = min(res, nums[mid])
        
        return res
            