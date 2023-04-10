'''
Intial thoughts create a list of count for each of the nums if two of them present add them to the solution
Sort the list in descending order allowing for a larger palindromic number

##
need some special case for the middle one qnd handling leading zeros
'''
class Solution:
    def largestPalindromic(self, num: str) -> str:
        ## special case for all zeroes
        
        s = set(num)
        s = list(s)
        #print(s)
        if len(s) == 1 and s[0] == '0':
            return "0"
        # if len(s) == 1 and s[0] == '0':
        #     return "0"
        frequency = {}
        
        for i in num:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        # print(frequency)
        ## creating a list of sinles and doubles
        ## blindly attach the double on both sides
        singles = []
        doubles = []
        for key in frequency:
            if frequency[key] % 2 == 1:
                singles.append(key)
                # since one of them is append, i decrease by 1
                frequency[key] -= 1
            for k in range(frequency[key]//2):
                doubles.append(key)
        
        # print(singles)
        # print(doubles)
        
        ### reverse both the list since I only want largets palindrome
        singles = sorted(singles, reverse = True)
        doubles = sorted(doubles, reverse = True)
        ans = ""
        for i in doubles:
            ans += i
        # appending the larget one from singles since we want largest
        if len(singles) > 0:
            ans += singles[0]
        # appending from doubles again since they are should be present at the end
        for i in doubles[::-1]:
            ans += i
        ans = list(ans)
        #print(ans)
        ## need to address the speacial case of 0
        while (len(ans) > 0):
            #exit condition if I don't find a leading zero
            if ans[0]!= '0':
                break
            if ans[0] == '0':
                #pop the first zero
                ans.pop(0)
                #pop the zero from the back because it is the first ones matching 
                ans.pop()
        return "".join(ans)
        
                
       