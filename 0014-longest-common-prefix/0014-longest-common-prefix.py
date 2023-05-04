class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # get the loength of the minimum word
        minlen = float("inf")
        for i in range(len(strs)):
            if len(strs[i]) < minlen:
                minlen = len(strs[i])
                word = strs[i] 
        ans = ''
        for i in range(len(word)):
            s = word[:i+1]
            flag = False
            for j in range(len(strs)):
                if strs[j][:i+1] != s:
                    flag = True
                    break
            if flag == False:
                ans = s
        return ans
            
            
            
        