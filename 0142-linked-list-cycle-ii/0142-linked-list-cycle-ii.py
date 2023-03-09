# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case:
        if not head:
            return None
        slow = head
        fast = head
        flag = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                flag = True
                break
        if flag:
            while head:
                if slow == head:
                    return head
                head = head.next
                slow = slow.next
                # if head == slow:
                #     return head
        return None