class Solution:
    def calculate(self, s: str) -> int:
        if s == " ":
            return
        stack = []
        operator = ("+","-","*","/")
        temp = 0
        op = '+'

        for i in range(len(s)):
            letter = s[i]
            if letter not in operator and letter != " ":
                temp = temp*10 + int(letter)
            if letter in operator or i == len(s)-1:
                if op == '+':
                    stack.append(temp)
                elif op == '-':
                    stack.append(-temp)
                elif op == '*':
                    temp = stack.pop()*temp
                    stack.append(temp)
                else:
                    dividend = stack.pop()
                    if dividend > 0:
                        stack.append(dividend//temp)
                    else:
                        stack.append(-1*((-dividend)//temp))
                op = letter
                temp = 0

        return(sum(stack))
            