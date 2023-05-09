# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        length = 0
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        curr = head
        while curr:
            curr = curr.next
            length += 1
        if length == 1:
            return None
        if length % 2 == 0:
            
            if slow.next and slow.next.next:
                slow.next = slow.next.next
            else:
                slow.next = None
        else:
            prev = ListNode(0, head)
            
            while prev.next != slow:
                prev = prev.next
            prev.next = prev.next.next
        
        return head