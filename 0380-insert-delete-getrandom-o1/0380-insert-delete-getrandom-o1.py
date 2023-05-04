class RandomizedSet(object):

    def __init__(self):
        self.l = []
        self.s = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.s:
            self.s.add(val)
            self.l.append(val)
            return True
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.s:
            return False
        self.s.remove(val)
        self.l.remove(val)
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        n = random.randint(0, len(self.l)-1)
        return self.l[n]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()