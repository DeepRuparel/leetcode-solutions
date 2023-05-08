class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.l = deque([])
        self.capacity = capacity
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = -1
        if key in self.d:
            val = self.d[key]
            self.l.remove(key)
            self.l.append(key)
        return val
            
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.l.remove(key)
            self.l.append(key)
            self.d[key] = value
        else:
            if len(self.l) == self.capacity:
                keytopop = self.l.popleft()
                self.d.pop(keytopop)
            self.d[key] = value
            self.l.append(key)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)