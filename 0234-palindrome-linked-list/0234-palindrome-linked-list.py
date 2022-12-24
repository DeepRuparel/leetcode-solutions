# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        curr = head
        prev = None
        while curr:
            count += 1
            curr = curr.next
        if count == 1:
            return True
        mid = count//2
        curr = head
        for i in range(mid):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        if count % 2 == 1:
            curr = curr.next
        
        for i in range(count):
            if curr and prev:
                if curr.val == prev.val:
                    curr = curr.next
                    prev = prev.next
                else:
                    return False
            
            elif not curr and not prev:
                return True
            else:
                return False
        