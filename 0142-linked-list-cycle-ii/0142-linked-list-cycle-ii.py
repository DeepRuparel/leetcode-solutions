# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# same approach as linked list cycle 

'''
now advance the head and slow until slow and head are equal this is your answer
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return 
        fast = slow = head
        foundCycle = 0
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                foundCycle = 1
                break
        
        if foundCycle:
            while head!= slow:
                head = head.next
                slow = slow.next
            return head
        else:
            return None
        