class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        
        for i in s:
            if i - 1 not in s:
                curr = i 
                curr_streak = 1
                while curr+1 in s:
                    curr+=1
                    curr_streak += 1
                longest = max(longest, curr_streak)
        return longest