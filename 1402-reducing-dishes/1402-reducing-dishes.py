class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        # if the previous solution along with the current one is better we update it else we dont
        # I know this a dp problem, so I need some way to compute the values beforehand maybe   
        '''
        one approach is to sort it   
        # lets see how it works in dry run
        I am assuming since we sort that
        we know what the max value is 
        save it if it positive
        [-9, -8, -1, 0, 5]
        
        so max = 5
        then check if abs(i) < max if yes we include it in the ans
        so we skip -9 and -8
        
        we include -1 so rn coeff = -1
        0 * 2 = 0 no change so include it 
        5 * 3 = 15 -1 + 15 > coeff so we indclude it 14
        
        This approach gives wrong answer error
        '''
        
        satisfaction = sorted(satisfaction)
        ans = 0
        csum = 0
        
        for i in satisfaction[::-1]:
            if i + csum > 0:
                csum += i
                ans += csum
        return ans