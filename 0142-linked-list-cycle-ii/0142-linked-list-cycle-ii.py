# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return 
        fast = slow = head 
        
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                break 
        else:
            return None
        while head!= slow:
            head = head.next 
            slow = slow.next 
        
        return head
        
        