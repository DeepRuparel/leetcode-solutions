class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #keep oushing until I fnd something I can pop
        
        stack = []
        index = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        
        if index == len(popped):
            return True
        return False
            
            