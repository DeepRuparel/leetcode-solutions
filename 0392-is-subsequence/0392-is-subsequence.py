class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i <len(t) and j< len(s):
            if t[i] == s[j]:
                i+=1
                j+=1
            else:
                i+=1   
        if j == len(s):
            return True
        else:
            return False