class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jewel_set = set(jewels)
        for i in stones:
            if i in jewel_set:
                ans+=1
        return ans
        