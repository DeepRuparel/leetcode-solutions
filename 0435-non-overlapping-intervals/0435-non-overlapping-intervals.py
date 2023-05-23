class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        remove = 0
        last = intervals[0][1]
        
        for i in intervals[1:]:
            if last > i[0]:
                last = min(last, i[1])
                remove+=1
            else:
                last = i[1]
        return remove