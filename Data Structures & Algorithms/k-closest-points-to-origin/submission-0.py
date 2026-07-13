class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time Complexity: O(nlogk)
        Space Complexity: O(k)
        """
        heap = []
        for x, y in points:
            dist = -1 * ((x ** 2 + y ** 2) ** 0.5)
            heapq.heappush(heap, [dist, x, y])

            if (len(heap) > k):
                heapq.heappop(heap)
        
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res
