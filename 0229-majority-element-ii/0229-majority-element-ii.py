class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        ans = []
        for i in nums:
            if i in d:
                d[i][0] += 1
                if d[i][0] > n//3 and d[i][1] != 1:
                    ans.append(i)
                    d[i][1] = 1
            else:
                d[i] = [1, 0]
                if d[i][0] > n//3:
                    ans.append(i)
                    d[i][1] = 1
        return ans
                