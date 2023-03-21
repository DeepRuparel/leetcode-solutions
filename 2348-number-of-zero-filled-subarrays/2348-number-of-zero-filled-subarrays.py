class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int: 
        curr_window = 0
        count = 0
        for i in nums:
            if i == 0:
                curr_window += 1
                count += curr_window
            else:
                curr_window = 0
        return count
        
        
        
        
        ############# Gives TLE ####################
        # curr_window = 0
        # count = 0
        # while True:
        #     prev_count = count
        #     for i in range(0, len(nums) - curr_window):
        #         if sum(nums[i : i + curr_window + 1]) == 0 and len(set(nums[i: i + curr_window + 1])) == 1:
        #             count += 1
        #     if count == prev_count:
        #         break
        #     curr_window += 1
        # return count