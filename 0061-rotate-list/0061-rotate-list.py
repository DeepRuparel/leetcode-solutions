'''
get the length of the list 
subtract k from it 
and go on traversing the list until n - k > 0
# note observed that k > n so do k = k % n
when the loop exits 
store the next node in temp and temphead
make the nodes'next as none
go until the end of temp make it's none point to head
make head = temp

dry run:
1 -> 2 -> 3 -> 4 -> 5

n = 5
k % 5 = 3 % 5 = 3
while k > 0
1 -> 2 -> 3 -> 4 -> 5
        here
        
temp = here.next
temphead = temp
make here.next = None
1 -> 2 -> 3 -> None. 4 -> 5
                     temp
                     tempHead
while temp.next != None
increase temp

after loop 
1 -> 2 -> 3 -> None. 4 ->       5 ->None
                    tempHead    temp
temp.next = Head

4 -> 5 -> 1 -> 2 -> 3 -> None
make tempHead = head
4 -> 5 -> 1 -> 2 -> 3 -> None
Head

This didn't work need to refine it

1 -> 2 -> 3 -> 4 -> 5
^ - -  -  -  -  -  -|
k = k % n
k = 2

curr = head

till n - k - 1 = 6 - 2 - 1 = 3
curr = curr.next

1 -> 2 -> 3 -> 4 -> 5
^ - - - - - - - - - |
          curr
curr.next = newhead
curr.next = none



temp = Head
go 
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head
        k = k % n
        curr = head
        for i in range(n - k - 1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        return newHead
        
       
            
        