# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
brute force:
traverse the list add them to a list conver the list to integer and reverse it add the it to the same of second list and then convert to list again and return as answer
time : o(max(n,m))
space : o(n+m)

optimized:
let carry be 0 -> just starting 
rtraverse the the two linkedklisrt at the same time
get the value of nodes 
if null make it zero
add the two lets say the addition is 11
take 11 % 10 which is 1. that is your what you append in the node 
and 11/10 which is 1 that is your new carry
keep on doing this until you reach the end of both the l;inked list 
return the head of new linked list
time : o(max(n,m))
pace : o(1)
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        head = dummyNode
        carry = 0
        
        while l1 or l2 or carry:
            if l1 is None:
                l1val = 0
            else:
                l1val = l1.val
            if l2 is None:
                l2val = 0
            else:
                l2val = l2.val
            addition = l1val + l2val + carry
            modulo = addition % 10
            carry = addition // 10
            dummyNode.next = ListNode(modulo)
            dummyNode = dummyNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        