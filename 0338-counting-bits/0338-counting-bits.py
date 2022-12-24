class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [n]
        dp = [0,1]
        for i in range(2,n+1):
            a = bin(i)
            dp.append(a.count('1'))
        return dp
        