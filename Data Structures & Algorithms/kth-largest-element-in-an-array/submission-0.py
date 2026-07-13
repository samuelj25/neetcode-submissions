class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1 * n for n in nums]
        heapq.heapify(heap)
        i = 1

        while (i < k):
            heapq.heappop(heap)
            i += 1
        
        return -1 * heap[0]