class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res