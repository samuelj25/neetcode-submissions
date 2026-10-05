class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        heap = []
        heapq.heapify(heap)

        for key, val in count.items():
            if (len(heap) >= k):
                if (heap[0][0] < val):
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
        
        res = []

        for _, num in heap:
            res.append(num)
        
        return res
