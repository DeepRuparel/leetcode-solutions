class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        n = list(set(nums))
        n = sorted(n)
        prev = 0
        for i in n:
            val = c.get(i)
            temp = val
            c[i] = prev
            prev = prev + temp
        ans = []
        for i in nums:       
            ans.append(c[i])
        return ans
        