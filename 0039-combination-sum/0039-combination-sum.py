class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(curr, rem, start):
            if rem < 0:
                return 
            elif rem == 0:
                output.append(curr[:])
            else:
                for i in range(start,len(nums)):
                    curr.append(nums[i])
                    backtrack(curr, rem-nums[i], i)
                    curr.pop()
        output = []
        nums = candidates
        backtrack([], target, 0)
        return output
#         ans = []
#         candidates.sort()
#         def dfs(candidates,target,path):
#             if target == 0:
#                 ans.append(path)
#             if target < candidates[0] or not candidates:
#                 return
#             for i, c in enumerate(candidates):
#                 dfs(candidates[i:], target-c, path+[c])
            
       
#         dfs(candidates,target,[])
#         return ans
        