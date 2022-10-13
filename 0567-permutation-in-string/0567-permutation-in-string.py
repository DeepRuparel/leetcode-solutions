from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        
        for i in range(len(s2)-len(s1)+1):
            if "".join(sorted(s2[i:i+len(s1)])) == s1:
                return True
        return False
        
        
        