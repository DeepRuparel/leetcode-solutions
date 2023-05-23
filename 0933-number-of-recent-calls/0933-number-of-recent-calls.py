class RecentCounter:

    def __init__(self):
        self.h = deque()
        

    def ping(self, t: int) -> int:
        self.h.append(t)
        
        while self.h[0] < t - 3000:
            self.h.popleft()
        
        return len(self.h)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)