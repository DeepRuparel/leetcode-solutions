class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []
        #heapq in python is always ascending so we need to put negative numbers value intyo it
        
        # go through all the nums and put in heap if number si even put as it is, if odd multiply by 2 and put it in heap
        
        m = float("inf")
        
        for num in nums:
            if num % 2 == 0:
                heapq.heappush(heap, -num)
                m = min(num, m)
            else:
                heapq.heappush(heap, -(num * 2))
                m = min(num * 2, m)
        ans = float("inf")
        #start popping from heap until heap is empty or you encounter an odd elment in the heap
        #print(heap)
        while heap:
            top = heapq.heappop(heap)
            top = top * -1
            ans = min(ans, top - m)
            if top % 2 != 0:
                break
            m = min(m, top//2)
            heapq.heappush(heap, -(top//2))
        return ans