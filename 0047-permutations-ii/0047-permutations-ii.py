class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, used):
            if len(curr) == len(nums):
                output.append(curr[:])
            else:
                for i in range(n):
                    if used[i] or i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                        continue
                    used[i] = True
                    curr.append(nums[i])
                    backtrack(curr, used)
                    used[i] = False
                    curr.pop()
        
        n = len(nums)
        nums = sorted(nums)
        output = []
        used = [False] * n
        backtrack([], used)
        return output