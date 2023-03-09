class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, rem, start):
            if rem < 0:
                return 
            elif rem == 0:
                ans.append(curr[:])
            else:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    curr.append(nums[i])
                    backtrack(curr, rem - nums[i] , i + 1)
                    curr.pop()
        
        
        
        
        
        nums = sorted(candidates)
        ans = []
        backtrack([], target, 0) #curr list, target, starting position
        
        return ans