class Solution:
    def simplifyPath(self, path: str) -> str:
        #"easier to split the path on '/'"
        
        ## splitting the path on '/'
        l = path.split('/')
        #stack of directories
        stack = []
        
        for d in l:
            #continue if string is null
            if d == '':
                continue
            elif d == '..':
                #check if stack present
                if stack:
                    stack.pop()
            
            elif d != '.':
                stack.append(d)
        
        
        return '/' + '/'.join(stack)
        
    
        
        
            
        
        