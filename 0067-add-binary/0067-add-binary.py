'''
let us convert the binary string to integer so like num * 2 + int(i)
add them and convert to binary and return without the 0n ahead

Time : o(max(m,n))
m = len(a)
n = len(b)
size : O(1)

Dry run:
11 -> 
i = 1
num1 = 0
num1 = num1 * 2 + i
so num1 = 1
i = 2
num1 = 1 * 2 + 1 
num1 = 3
similarly for num 2
num1 = 3 num2 = 1
ans = num1 + num2
ans = 4
return ans binary so 0b100 return 100 as string
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = 0
        num2 = 0
        
        for i in a:
            num1 = num1 * 2 + int(i)
        for i in b:
            num2 = num2 * 2 + int(i)
        
        ans = num1 + num2
        return "{0:b}".format(ans)
        