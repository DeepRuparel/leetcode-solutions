class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        ans = []
        
        for interval in intervals:
            if ans == []:
                ans.append(interval)
            if ans[-1][1] >= interval[0]:
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans.append(interval)
        return ans