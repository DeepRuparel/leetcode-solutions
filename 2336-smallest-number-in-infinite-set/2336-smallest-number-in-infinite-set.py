import heapq
from queue import PriorityQueue
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = set()
        self.q = PriorityQueue()
        for i in range (1, 1001):
            self.heap.add(i)
            self.q.put(i)
        

    def popSmallest(self) -> int:
        
        if self.q:
            next = self.q.get()
            self.heap.remove(next)
            return next
        

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            self.heap.add(num)
            self.q.put(num)
       
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)