class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_one, candidate_two = None, None
        k = len(nums) // 3
        count_one, count_two = 0, 0
        res = []

        for num in nums:
            if (count_one == 0):
                candidate_one = num
                count_one += 1
            elif (num != candidate_one) and (count_two == 0):
                candidate_two = num
                count_two += 1
            elif (num == candidate_one):
                count_one += 1
            elif (num == candidate_two):
                count_two += 1
            elif (num != candidate_one) and (num != candidate_two):
                count_one -= 1
                count_two -= 1
        
        count_one, count_two = 0, 0
        for num in nums:
            if num == candidate_one:
                count_one += 1
            elif num == candidate_two:
                count_two += 1
        
        if count_one > k:
            res.append(candidate_one)
        if count_two > k:
            res.append(candidate_two)
        
        return res
