# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy 
        curr = head
        
        while curr and curr.next:
            nextNode = curr.next.next
            second = curr.next
            
            prev.next = second
            second.next = curr
            curr.next = nextNode
            
            prev = curr
            curr = nextNode
        return dummy.next
        
            
#         head2 = ListNode()
#         head3 = head2
        
#         nums = []
#         while head:
#             nums.append(head.val)
#             head = head.next
        
#         for i in range(0,len(nums)-1,2):
#             nums[i],nums[i+1] = nums[i+1], nums[i]
        
#         for i in nums:
#             head2.next = ListNode(i)
#             head2 = head2.next
#         return head3.next
            