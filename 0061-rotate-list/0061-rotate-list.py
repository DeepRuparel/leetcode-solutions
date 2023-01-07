# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 1
        
        curr = head
        while curr.next:
            length+=1
            curr = curr.next
        
        curr.next = head
        
        curr = head
        k %= length
        for i in range(length-k-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        return newHead
        
#         length = 1
#         curr = head
#         while curr.next:
#             length+=1
#             curr = curr.next
#         #print(curr.val)
#         curr.next = head
#         curr = head
        
#         k %= length
#         for i in range(length-k-1):
#             curr = curr.next
#         #print(curr.val)
#         newhead = curr.next
#         curr.next = None
#         return newhead
            
        