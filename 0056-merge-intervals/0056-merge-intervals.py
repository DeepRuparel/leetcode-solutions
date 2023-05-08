class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        ans.append(intervals.pop(0))
        #print(ans)
        #return ans
        for interval in intervals:
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans.append(interval)
        return (ans)
        return [[]]
                