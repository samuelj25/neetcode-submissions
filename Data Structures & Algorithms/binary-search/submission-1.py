class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            half = (l + r) // 2
            curr = nums[half]

            if curr == target:
                return half
            elif curr > target:
                r = half - 1
            else: # curr < target
                l = half + 1

        return -1
