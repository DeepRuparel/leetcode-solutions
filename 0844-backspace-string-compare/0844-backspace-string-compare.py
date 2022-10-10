class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        
        for i in s:
            if i == '#' and s_stack:
                s_stack.pop()
            elif i== '#' and s_stack == []:
                continue
            else:
                s_stack.append(i)
        for i in t:
            if i == '#' and t_stack:
                t_stack.pop()
            elif i== '#' and t_stack == []:
                continue
            else:
                t_stack.append(i)
        return s_stack == t_stack
        