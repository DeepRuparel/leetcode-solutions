from collections import Counter
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        maximum = max(nums) + 1
        hashmap = Counter(nums)
        # print(hashmap)
        
        prefix_sum = [0] * maximum
        
        for i in range(1,maximum):
            if i not in hashmap:
                prefix_sum[i] = prefix_sum[i-1]
            else:
                prefix_sum[i] = prefix_sum[i-1] + hashmap[i]
        #print(prefix_sum)
        summ = 0
        for i in (set(nums)):
            for j in range(i,maximum,i):
                summ += hashmap[i] * (prefix_sum[-1]-prefix_sum[j-1])
        return summ % (10**9 +7)
        
        
        
#         maxi = max(nums) + 1
#         dic = {}
#         prefix=[0]*maxi
#         for i in nums:
#             if i in dic:
#                 dic[i] += 1
#             else:
#                 dic[i] = 1
#         #print(dic)
#         for i in range(1,maxi):
#             if i not in dic:
#                 prefix[i] = prefix[i-1]
#             else:
#                 prefix[i] = prefix[i-1]+dic[i]
        
#         sumP = 0
#         for i in set(nums):
#             for j in range(i,maxi,i):
#                 print(i, end = " ")
#                 sumP += dic[i]*(prefix[-1]-prefix[j-1])
#                 print(sumP)