class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rq = deque()
        dq = deque()
        
        for i, s in enumerate(senate):
            if s == "R":
                rq.append(i)
            else:
                dq.append(i)
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            
            if d < r:
                dq.append(d + n)
            else:
                rq.append(r + n)
        if rq:
            return "Radiant"
        return "Dire"