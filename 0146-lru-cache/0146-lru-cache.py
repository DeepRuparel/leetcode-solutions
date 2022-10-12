class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.queue = deque()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.queue.remove(key)
            self.queue.append(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.queue.remove(key)
            self.queue.append(key)
            self.d[key] = value
        else:
            if len(self.queue) == self.capacity:
                k = self.queue.popleft()
                self.d.pop(k)
            self.queue.append(key)
            self.d[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)