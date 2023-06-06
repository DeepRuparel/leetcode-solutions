class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mine , maxe = min(arr), max(arr)
        n = len(arr)
        s = set()
        
        if maxe-mine == 0:
            return True
        if (maxe - mine) % (n-1):
            return False
        diff = (maxe - mine) // (n-1)
        
        for i in arr:
            if (i - mine) % diff:
                return False
            s.add(i)
        return len(s) == n