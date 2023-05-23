class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                curr = stack.pop()
                ans[curr] = i - curr
            stack.append(i)
        return ans
        