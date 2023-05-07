class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        if self.minheap == []:
            heappush(self.minheap, -num)
            return
        if num <= -self.minheap[0]:
            heappush(self.minheap, -num)
        else:
            heappush(self.maxheap, num)
        
        if len(self.minheap) - len(self.maxheap) == 2:
            heappush(self.maxheap, -heappop(self.minheap))
        elif len(self.minheap) - len(self.maxheap) == -2:
            heappush(self.minheap, -heappop(self.maxheap))
            
        

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (-self.minheap[0]+self.maxheap[0])/ 2.0
        if len(self.maxheap) > len(self.minheap):
            return float(self.maxheap[0])
        else:
            return float(-self.minheap[0])
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()