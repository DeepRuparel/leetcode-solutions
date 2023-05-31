class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        ans = []
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > n//3 and i not in ans:
                    ans.append(i)
            else:
                d[i] = 1
                if d[i] > n//3:
                    ans.append(i)
        return ans
                