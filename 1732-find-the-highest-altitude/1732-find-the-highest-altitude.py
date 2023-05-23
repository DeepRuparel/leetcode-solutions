class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0]
        max1 = ans[0]
        for i in range(len(gain)):
            ans.append(gain[i] + ans[-1])
            if ans[-1] > max1:
                max1 = ans[-1]
        return max1