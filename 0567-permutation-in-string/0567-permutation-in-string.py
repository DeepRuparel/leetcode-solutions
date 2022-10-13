from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        
        for i in range(len(s2)-len(s1)+1):
            c2 = Counter(s2[i:i+len(s1)])
            if c2 == c:
                return True
        return False
        
        