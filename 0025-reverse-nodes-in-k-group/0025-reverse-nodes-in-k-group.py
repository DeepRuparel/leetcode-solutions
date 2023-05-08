# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def getkth(curr, k):
            while k and curr:
                curr = curr.next
                k-=1
            return curr
        
        dummy = ListNode(0, head)
        groupprev = dummy
        
        while True:
            kth = getkth(groupprev, k)
            if not kth:
                break
            
            prev = kth.next
            curr = groupprev.next
            groupnext = kth.next
            
            while curr != groupnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp
        return dummy.next
            
        
        
        
        