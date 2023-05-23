class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        end = points[0][1]
        
        for i in range(1,len(points)):
            end = min(end, points[i][1])
            if points[i][0] <= end <= points[i][1]:
                continue
            else:
                arrows+=1
                end = points[i][1]
        return arrows