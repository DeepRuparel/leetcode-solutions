class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums = nums + nums
        ans = []
        for i in range(n):
            start = i
            flag = True
            for j in range(start + 1, start + n):
                if nums[start] < nums[j]:
                    ans.append(nums[j])
                    flag = False
                    break
            if flag:
                ans.append(-1)
        return ans
        