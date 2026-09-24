class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x == y:
                continue
            else:
                val = y - x
                heapq.heappush(heap, -val)

        return -heap[0] if heap else 0