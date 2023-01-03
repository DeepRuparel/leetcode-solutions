class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start = 0, curr = []):
            # if len(curr) == k:
            output.append(curr[:])
            
            for i in range(start, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        output = []
        n = len(nums)
        # for k in range(n+1):
        backtrack()
        return output