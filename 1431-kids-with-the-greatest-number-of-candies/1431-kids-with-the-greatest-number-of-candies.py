class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        orignal_max = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= orignal_max:
                ans.append(True)
            else:
                ans.append(False)
        return ans
                