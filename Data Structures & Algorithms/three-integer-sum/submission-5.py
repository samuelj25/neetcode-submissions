class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        nums.sort() # O(nlogn)
        res = []

        # [-4, -1, -1, 0, 1, 2]
        for i, value in enumerate(nums):
            if (value > 0):
                break

            if ((i > 0) and (value == nums[i - 1])):
                continue
    
            l, r = i + 1, len(nums) - 1
            while (l < r):
                three_sum = value + nums[l] + nums[r]

                if (three_sum == 0):
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while ((nums[l] == nums[l - 1]) and (l < r)):
                        l += 1
                elif (three_sum < 0):
                    l += 1
                else:
                    r -= 1
        
        return res
