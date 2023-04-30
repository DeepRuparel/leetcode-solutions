from queue import PriorityQueue 
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        q = PriorityQueue()
        for i in d:
            q.put((-d[i], i))
        s = ""
        while not q.empty():
            i, j = q.get()
            s += j*(-1 * i)
        #print(s)
            
        return s
                
        