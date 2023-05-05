class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        newstack = {'min': val, "max": val}
        if self.minstack:
            n = self.minstack[-1]
            newstack["min"] = min(newstack["min"], n["min"])
            newstack["max"] = min(newstack["max"], n["max"])
        self.minstack.append(newstack)
        self.stack.append(val)
            

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]["min"]
        return -1
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()