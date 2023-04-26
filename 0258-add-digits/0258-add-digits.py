class Solution:
    def addDigits(self, num: int) -> int:
        while num//10 > 0:
            ans = 0
            for i in str(num):
                ans += int(i)
            num = ans
        return num