class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float("inf")
        for i in range(len(blocks)-k+1):
            
            s = blocks[i:i+k]
            #print(s)
            ans = min(ans, s.count("W"))
        if ans == float("inf"):
            return 0
        return ans