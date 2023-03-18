'''
Thought of a doubly linkedlist but wouldn't work
making use of two stacks
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = []
        self.to_visit = []
        self.current = homepage

    def visit(self, url: str) -> None:
        self.visited.append(self.current)
        self.current = url
        self.to_visit = []

    def back(self, steps: int) -> str:
        
        while steps > 0 and self.visited:
            self.to_visit.append(self.current)
            self.current = self.visited.pop()
            steps -= 1
        return self.current
        

    def forward(self, steps: int) -> str:
        while steps and self.to_visit:
            self.visited.append(self.current)
            self.current = self.to_visit.pop()
            steps -= 1
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)