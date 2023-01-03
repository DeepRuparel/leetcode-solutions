class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start = 0, curr = []):
            # if len(curr) == k :
            output.append(curr[:])
            # else:
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        output = []
        n = len(nums)
        nums = sorted(nums)
        # for k in range(n+1):
        backtrack()
        return output
        