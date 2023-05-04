'''
approach use 2 for loops one fopr the rownumber other to append the the next things to it.
Observation in case of 3 next item to append is present at 4
in case of 4 it is 6
so 2 * numrows -1 
for first row and last row no need to append characters in begining
for middle rows we can seeincase of rownumber 2 we need to append P wghich is 2 spacs from A , L which is two spaces from P and so on
so increment - 2 * currentrownumber

Dry run 
s = "PAYPALISHIRING" n = 4
so we know for first row it is 2 * (4-1) = 6 so increrment actor is 6
P -> 6 I -> N

for r = 2
we know we need to append letters presetn in increment of 6
so 
A ->6 S ->6 G
but also L and I 
which are 4 spaces from A and S respectivels so 
append increment - 2 * cureentrownumber so 6 - 2 = 4
A -> 4 L ->6 from A -> S -> 4 from(S) -> I -> 6(from S) > G

for r = 3
also incluse increment - 2 * currentrownumber = 6 - 4 = 2 

Y ->2 from(y) A -> 6 from (y) H -> 2 from (h) R and end

for last row r = 4
just appned letters present at increment
P , I
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = ""
        increment = 2 * (numRows - 1)
        for r in range(numRows):
            for i in range(r, len(s), increment):
                ans += s[i]
                if r > 0 and r < numRows - 1 and i + increment - 2 * (r) < len(s):
                    ans += s[ i + increment - 2 * r]
        return ans