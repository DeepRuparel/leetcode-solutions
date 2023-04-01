'''
Thinking of something like having a priority queue because I want everythhing sorted in ascending order
and a stack to keep track of all the assigned seats so incase I have something unreserved I pop from stack the  seat and pass it to priority queue
I pop the first element from the priority queue to get the lowest unreserved seats

Recived TLE once then changed to set instead of a stack so TLE was beaten.
'''
"""
Trying to use heap.
"""
from queue import PriorityQueue
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.h = []
        for i in range(1, n+1):
            self.h.append(i)
        heapq.heapify(self.h)

    def reserve(self) -> int:
        return heapq.heappop(self.h)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)