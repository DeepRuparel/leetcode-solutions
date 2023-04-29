"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
need to do a level order level travesal
when i am done with oe level I know the last node now in the queue is the the rightmost node on that level mark it wil something so you know all nodes uptil that node have next as the left most element of the queue and the node with lets say '#' will have its next as none

Dry run:
q = [1]
root.next = None
1 -> None
while q 
for i in range(len(q))
pop it out
a = 1
put 2 and 3 in q
now q = [2,3]
we know 3 -> next is None
so mark 3 -> '#'
pop from q
a = 2
is 2 -> next = '#'
no so
2 -> next is 3 in picture andf 3 is currently at q[0]
so 2 -> next = q[0] so 2-> next = 3
add 4 and 5 to q
a = 3
3 -> next == '#' so we know we mark it as None
3 -> next = None
add 7 to q
q = [4 , 5, 7] now 7 -> next should be None so mark it's next as None
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        root.next = None
        while q:
            for _ in range(len(q)):
                a = q.popleft()
                if a.next != '#' and q:
                    a.next = q[0]
                else:
                    a.next = None
                
                if a.left :
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            if q:
                q[-1].next = '#'
        return root
        
        
        
        
        
        
        
        
        
        
        
       
                    
        