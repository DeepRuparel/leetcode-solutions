class Solution:
    def average(self, salary: List[int]) -> float:
        
        
        minimum = min(salary)
        maximum = max(salary)
        
        s = (sum(salary) - minimum - maximum)/ (len(salary) - 2)
        return s