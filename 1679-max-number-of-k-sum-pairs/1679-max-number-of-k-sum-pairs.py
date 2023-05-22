class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        for i in range(len(nums)):
            rem = k - nums[i]
            if rem in d:
                count += 1
                if d[rem] == 1:
                    del d[rem]
                else:
                    d[rem] -= 1
            else:
                if nums[i] in d:
                    d[nums[i]] += 1
                else:
                    d[nums[i]] = 1
        return count
                