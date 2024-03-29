# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        # ans = head
        # while head and head.next:
        #     prev = head.val
        #     if head.next.val == prev:
        #         head.next = head.next.next
        #     else:
        #         head = head.next
        # return ans
                
        ans = head
        
        while head.next:
            prev = head.val 
            if head.next.val == prev:
                head.next = head.next.next
            else:
                head = head.next
        return ans