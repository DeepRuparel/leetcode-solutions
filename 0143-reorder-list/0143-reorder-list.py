# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head 
        
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        n = slow.next 
        slow.next = None
        
        prev = None 
        while n:
            temp = n.next 
            n.next = prev 
            prev = n
            n = temp 
        n = head 
        while prev:
            temp = n.next 
            tempprev = prev.next 
            n.next = prev 
            prev.next = temp 
            n = temp
            prev = tempprev
        
        return head
        