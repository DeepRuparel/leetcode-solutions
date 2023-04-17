class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        
        curr_sum = 0
        ans = float("inf")
        
        # traverse the given nums
        
        while right < len(nums):
            #adding the current number to sum
            curr_sum += nums[right]
            
            #check if curr sum if less than target which means I can add more things to it
            
            if curr_sum < target:
                right += 1
            
            else:
                # this means I need to keep removing numbers from the left until the sum is less than target
                while curr_sum >= target:
                    #geeting the current size of the numbers which lead to curr_sum
                    ans = min(ans, right - left + 1)
                    # removing the leftmost element
                    curr_sum -= nums[left]
                    #incrementing left
                    left += 1
                
                right += 1
        if ans == float('inf'):
            return 0
        else:
            return ans