class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {}
        d[0] = 1
        presum = 0
        ans = 0
        for num in nums:
            presum+=num
            if presum - k in d:
                ans+= d[presum-k]
            d[presum] = d.get(presum,0)+1
        return ans