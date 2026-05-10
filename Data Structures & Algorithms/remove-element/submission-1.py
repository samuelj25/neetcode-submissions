class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        res = 0

        while left <= right:
            if nums[right] == val:
                right -= 1
            else:
                if nums[left] == val:
                    nums[left] = nums[right]
                    left += 1
                    right -= 1
                else:
                    left += 1
                res += 1
        return res