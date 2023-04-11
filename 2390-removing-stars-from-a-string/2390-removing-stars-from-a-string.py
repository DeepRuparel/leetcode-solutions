class Solution:
    def removeStars(self, s: str) -> str:
        # convert the string to list
        
        l = []
        for i in s:
            if i != "*":
                l.append(i)
            elif i == "*":
                l.pop()
        
        return "".join(l)        