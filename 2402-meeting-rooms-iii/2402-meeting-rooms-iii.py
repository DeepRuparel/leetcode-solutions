class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        
        availrooms = []
        busy = []
        # sorted meetings on start time
        meetings.sort()
        
        # creatinf a min heap of availrooms since all of them are available
        for i in range(n):
            heapq.heappush(availrooms, i)
            
        rooms = [0] * n
        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]
            
            while len(busy) > 0 and busy[0][0] <= start:
                heapq.heappush(availrooms, busy[0][1])
                #print(busy)
                heapq.heappop(busy)
            
            if len(availrooms) > 0:
                top = availrooms[0]
                rooms[top] += 1
                heapq.heappop(availrooms)
                temp = [end, top]
                #print(temp)
                heapq.heappush(busy, temp)
                continue
            temp2= busy[0]
            #print(temp2[0], temp2[1])
            end_curr = temp2[0]
            roomid = temp2[1]
            heapq.heappop(busy)
            rooms[roomid] += 1
            newtemp = [end_curr + end - start , roomid]
            heapq.heappush(busy, newtemp)
        return rooms.index(max(rooms))
            