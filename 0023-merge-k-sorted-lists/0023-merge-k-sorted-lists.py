'''
Brute force:
merge k list into and sort them
time : o (N log N) N = sum of length of all lists
space = O(N)

Dry run:
q = [] //prioirty queue based on val
q = [(1 -> [val : 1, next->4,5]), (1, val : 1 ->(3, 4), 2, val : 2 -> 6 ]
pop first one out 
we get 
val = 1
node = 1 -> 4 -> 5
add 1 to result
node = node.next = 4
if node.next add 4 and 4 -> to q
q = [(1, val : 1 ->(3, 4), (2, val : 2 -> 6), 4. val : 4 -> 5 ]
again pop 
so 
val = 1
node = 1 -> 3 > 4
append 1 to ans
add 3, 3 ->4 to q
q = [(2, val : 2 -> 6), (3, val : 3 -> 4),(4, val : 4 -> 5 )]
and so on

Time : O(N) N -> sum of length of all the lists
size : O(size(lists))
'''

from Queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = head = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        #while q is no empyth start poppping from them
        while not q.empty():
            val, node = q.get()
            head.next = ListNode(val)
            head = head.next
            node = node.next
            #check if node is not none
            if node:
                q.put((node.val, node))
        return ans.next
            
        