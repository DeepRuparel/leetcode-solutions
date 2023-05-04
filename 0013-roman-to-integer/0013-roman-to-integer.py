class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        create a dictionary of order
        I : 1 V : 2 X : 3 L : 4 C : 5 D : 6 M : 7
        MCMXCIV
        i = 0 M
        M < C no so add value to ans ans = 1000
        i = 1
        C < M yes so add value to ans = 1000-100 = 900 + 1000 = 1900
        i = 3
        X < C yes so add 100-10 to ans 1900+90 = 1990
        i = 5
        I < V yes so add 4 to ans 
        i = 7
        out. of bound return ans
        '''
        order = {'I' : 1, 'V' : 2, 'X': 3, 'L' : 4, 'C' : 5, 'D' : 6, 'M' : 7}
        value = {'I' : 1,  'V' : 5, 'X' : 10, 'L' : 50,  'C' : 100,  'D' : 500,  'M' : 1000}
        
        i = 0
        n = len(s)
        ans = 0
        while i < n:
            if i + 1 < n:
                if order[s[i]] < order[s[i+1]]:
                    ans += value[s[i+1]] - value[s[i]]
                    i += 2
                else:
                    ans += value[s[i]]
                    i += 1
            else:
                ans += value[s[i]]
                i += 1
        return ans
                    