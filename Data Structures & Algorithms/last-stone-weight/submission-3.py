class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * n for n in stones]
        heapq.heapify(heap)

        while (len(heap) > 1):
            num_one = heapq.heappop(heap) * -1
            num_two = heapq.heappop(heap) * -1

            if (num_one > num_two):
                heapq.heappush(heap, (num_one - num_two) * -1)
        
        return heap[0] * -1 if heap else 0
