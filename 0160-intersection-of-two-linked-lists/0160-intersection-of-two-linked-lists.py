# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = 0
        head1 = headA
        while head1:
            head1 = head1.next
            n1 += 1
        n2 = 0
        head2 = headB
        while head2:
            head2 = head2.next
            n2 += 1
        
        if n1 > n2:
            for i in range(n1 - n2):
                headA = headA.next
        elif n2 > n1:
            for i in range(n2 - n1):
                headB = headB.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
            
            