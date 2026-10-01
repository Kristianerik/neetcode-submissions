class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
        heapq.heapify(self.smallHeap)
        heapq.heapify(self.largeHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)

        if self.smallHeap and self.largeHeap and (-self.smallHeap[0] > self.largeHeap[0]):
            heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))
            heapq.heappush(self.smallHeap, -heapq.heappop(self.largeHeap))

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))
        elif len(self.largeHeap) > len(self.smallHeap) + 1:
            heapq.heappush(self.smallHeap, -heapq.heappop(self.largeHeap))

        

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            return float((-self.smallHeap[0] + self.largeHeap[0]) / 2)
        elif len(self.smallHeap) > len(self.largeHeap):
            return float(-self.smallHeap[0])
        else:
            return float(self.largeHeap[0])

        