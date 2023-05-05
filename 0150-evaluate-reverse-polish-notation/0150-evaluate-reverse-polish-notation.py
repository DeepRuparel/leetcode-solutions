class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in ('+',"-","*","/"):
                stack.append(int(i))
            else:
                #print(stack)
                if i == '+':
                    stack.append(stack.pop()+stack.pop())
                elif i == '-':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second - first)
                elif i == '*':
                    stack.append(stack.pop()*stack.pop())
                else:
                    
                    first = stack.pop()
                    second = stack.pop()
                    #print(first,second)
                    sign = 1
                    if first < 0:
                        first *= -1
                        sign *= -1
                    if second < 0:
                        sign *= -1
                        second *= -1
                    ans = second//first
                    #print(ans)
                    stack.append(ans*sign)
        return stack[0]
                        
                        
            