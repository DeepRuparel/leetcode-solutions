'''
Brute force:
use the % and divide to get individual digit and append the list
add it to the list above from going backward and return the list as answer 

Time: o(max(n,k))
space : o(k)
dry run:
num = [1, 2, 3, 4]
k = 34 

tempk = []
k % 10 = 34 % 10 = 4
tempk = [4]
k // 10 = 3
k % 10 = 3
tempk = [3,4]
k // 10 = 0

start from the back of both the list
carry = 0
4 3 2 1
^
4 3
^
s = 4+4 + carry = 8
rem = s % 10 8 % 10 = 8
carry = s // 10 8 // 10
num[i] = 8
8 3 2 1
  ^
4 3
  ^
s = 3 + 3 + carry = 6
6 % 10 = 6
6 // 10 = 0
num [i] = 6
8 6 2 1
    ^
4 3

8 6 2 1
      ^
done
return 8 6 2 1
'''

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        tempk = []
        while k:
            rem = k % 10
            tempk.append(rem)
            k = k // 10
        
        num_size = len(num) - 1
        k_size = 0
        carry = 0
        ans = []
        while num_size >= 0 or k_size < len(tempk):
            if num_size >= 0:
                a = num[num_size]
            else:
                a = 0
            if k_size < len(tempk):
                b = tempk[k_size]
            else:
                b = 0
            s = a + b + carry
            rem = s % 10
            carry = s // 10
            ans.append(rem)
            num_size -= 1
            k_size += 1
        if carry:
            ans.append(carry)
        return ans[::-1]
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        