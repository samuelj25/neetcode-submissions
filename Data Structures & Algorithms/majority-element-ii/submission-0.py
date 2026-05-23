class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        res = []
        k = len(nums) // 3
        for key, val in count.items():
            if val > k:
                res.append(key)
        
        return res