class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        
        for course,prerequisite in prerequisites:
            prereq[course].append(prerequisite)
        cycle = set()
        output = []
        visited = set()
            
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for c in prereq[course]:
                if dfs(c) == False:
                    return False
            cycle.remove(course)
            output.append(course)
            visited.add(course)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output
            