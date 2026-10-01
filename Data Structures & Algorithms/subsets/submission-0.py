class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res_len = len(res)
            for i in range(res_len):
                temp = res[i].copy()
                temp.append(num)
                res.append(temp)
        
        return res
