class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for course, prerequisite in prerequisites:
            prereq[course].append(prerequisite)
        
        output = []
        visited = set()
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for prerequisite in prereq[course]:
                if dfs(prerequisite) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
                
        return True
                
            