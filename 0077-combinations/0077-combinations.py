from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = []
        # for i in range(1,n+1):
        #     nums.append(i)
        # ans = combinations(nums,k)
        # return ans
        
        def backtrack(start, curr):
            if len(curr) == k:
                output.append(curr[:])
            else:
                for i in range(start, n+1):
                    curr.append(i)
                    backtrack(i+1, curr)
                    curr.pop()
        output = []
        backtrack(1,[])
        return output