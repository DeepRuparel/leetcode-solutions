class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        mergednums = [(x,y) for x,y in zip(nums1, nums2)]
        mergednums.sort(key = lambda x : -x[1])
        #print(mergednums)
        topkelemets = []
        for i in range(k):
            topkelemets.append(mergednums[i][0])
        topksum = sum(topkelemets)
        heapq.heapify(topkelemets)
        answer = topksum * mergednums[k-1][1]
        for i in range(k, len(mergednums)):
            topksum -= heapq.heappop(topkelemets)
            topksum += mergednums[i][0]
            heapq.heappush(topkelemets, mergednums[i][0])
            
            answer = max(answer, topksum * mergednums[i][1])
            
        return answer
        