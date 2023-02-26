'''
This problem utilizes the levenstine distance 
The algo for it is
if word1[i] == word2[i]
cost = 0
else
cost = 1
dist[i][j] = min(oen above ie d[i-1][j] +1, one to the left ir d[i][j-1] +1 , one in diagonal d[i-1][j-1] + cost )

return diist[n][m] is your answet
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # get the n and m which is length of word1 and length of word2
        n = len(word1) 
        m = len(word2) 
        
        #base conditons
        if n == 0:
            return m
        if m == 0:
            return n
        #intsialize the distance array which is a 2d array of n * m
        dist = [[None for x in range(m + 1)] for y in range(n + 1)]  
        #print(dist)
        #intialize d[0][i] with i
        for i in range(n + 1):
            dist[i][0] = i
        #inialize d[j][0] with j 
        for j in range(m + 1):
            dist[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                #check if the two words at current index are same
                if word1[i - 1] == word2[j - 1]:
                    cost = 0
                else:
                    cost = 1
                #print(i,j)
                dist[i][j] = min(dist[i-1][j] + 1, dist[i][j - 1] + 1, dist[i - 1][j - 1] + cost)
        return dist[n][m]