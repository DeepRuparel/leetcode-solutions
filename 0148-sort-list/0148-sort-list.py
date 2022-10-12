# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        mid = self.mid(head)
        mid1 = mid.next
        mid.next = None
        
        l = self.sortList(head)
        r = self.sortList(mid1)
        
        res = self.merge(l,r)
        
        return res
    def merge(self,l,r):
        if not l:
            return r
        if not r:
            return l
        res = None
        if l.val < r.val:
            res = l
            res.next = self.merge(l.next,r)
        else:
            res = r
            res.next = self.merge(l,r.next)
        return res
    def mid(self,head):
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            
        