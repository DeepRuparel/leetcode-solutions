class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        curr_sum = 0
        max_sum = 0
        l = 0
        for num in nums:
            while num in seen:
                curr_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            curr_sum += num
            seen.add(num)
            max_sum = max(curr_sum,max_sum)
        return max_sum
                