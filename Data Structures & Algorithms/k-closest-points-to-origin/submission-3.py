class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time Complexity: O(nlogk)
        Space Complexity: O(k)
        """
        heap = []
        for point in points:
            dist = -1 * ((point[0] ** 2 + point[1] ** 2) ** 0.5)
            heapq.heappush(heap, [dist, point])

            if (len(heap) > k):
                heapq.heappop(heap)
        
        res = []
        while heap:
            _, point = heapq.heappop(heap)
            res.append(point)
        
        return res
