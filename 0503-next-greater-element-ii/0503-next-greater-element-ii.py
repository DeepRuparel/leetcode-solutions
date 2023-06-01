class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        ans = [-1] * len(nums)
        n = len(nums)
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if stack:
                ans[i % n] = stack[-1]
            else:
                ans[i % n] = -1
            stack.append(nums[i%n])
        return ans