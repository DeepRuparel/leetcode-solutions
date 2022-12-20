class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        canEnter = True
        keys = deque([0])
        unvisited = set(range(len(rooms)))
        #print(keys)
        while keys:
            key = keys.popleft()
            if key in unvisited:
                unvisited.remove(key)
                keys.extend(rooms[key])
        
        #print(visited)
        return not(unvisited)
                    
                
            
            