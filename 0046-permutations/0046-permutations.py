class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack( curr = []):
            if len(curr) == len(nums):
                output.append(curr[:])
            else:
                for i in range(n):
                    if nums[i] in curr:
                        continue
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
        output = []
        n = len(nums)
        # for k in range(n+1):
        backtrack()
        return output
        