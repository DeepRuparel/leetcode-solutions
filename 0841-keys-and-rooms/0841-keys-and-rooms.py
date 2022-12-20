class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        canEnter = True
        keys = [[0]]
        visited = set()
        while keys:
            i = keys.pop(0)
            for key in i:
                if key not in visited:
                    visited.add(key)
                    keys.append(rooms[key])
        
        #print(visited)
        return len(visited)==len(rooms)
                    
                
            
            