class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        if secondList == []:
            return ans
        if firstList == []:
            return ans
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            l = max(firstList[i][0], secondList[j][0])
            h = min(firstList[i][1] , secondList[j][1])
            if l<=h:
                ans.append([l,h])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return ans
        