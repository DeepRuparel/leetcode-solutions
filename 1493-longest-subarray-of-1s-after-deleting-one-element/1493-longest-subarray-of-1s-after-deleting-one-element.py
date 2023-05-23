class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = -1
        noofones = 0
        ans = -1
        prevleft = -1
        for right in range(len(nums)):
            if nums[right] == 0 and left == -1:
                left = right
            elif nums[right] == 0 and left != -1:
                temp = left
                while left > prevleft:
                    if nums[left] == 1:
                        if noofones:
                            noofones -= 1
                    left -= 1
                prevleft = temp
                left = right
            elif nums[right] == 1:
                noofones += 1
                ans = max(ans, noofones)
        if ans == -1 and left != -1:
            return 0
        if left == -1 and noofones > 0:
            return ans - 1
        return ans
                
                        
        