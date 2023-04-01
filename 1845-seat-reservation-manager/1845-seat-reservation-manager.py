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
class SeatManager:

    def __init__(self, n: int):
        self.q = PriorityQueue()
        for i in range(1, n+1):
            self.q.put(i)

    def reserve(self) -> int:
        n = self.q.get()
        return n

    def unreserve(self, seatNumber: int) -> None:
        
        self.q.put(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)