class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == '(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if not stack:
                    return False
                c = stack.pop()
                if i==')' and c!='(':
                    return False
                if i == ']' and c != '[':
                    return False
                if i == '}' and c != '{':
                    return False
                
        if stack:
            return False
        else:
            return True
                
                