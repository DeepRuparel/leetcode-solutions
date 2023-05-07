class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #targetelement = len(nums) - k
        
        h = []
        length = 0
        for i in nums:
            heapq.heappush(h, i)
            length += 1
            if length > k:
                heapq.heappop(h)
                length -= 1
        
        return h[0]
            
                    
                