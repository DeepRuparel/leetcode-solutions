class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left = 0
        # right = len(nums)
        # ans = []
        # pos = -1
        # if nums == []:
        #     return [-1,-1]
        # while left < right:
        #     mid = (left + right)//2
        #     if nums[mid] == target:
        #         pos = mid
        #         break
        #     elif nums[mid] > target:
        #         right-=1
        #     else:
        #         left += 1
        # if pos == -1:
        #     return [-1,-1]
        # else:
        #     i , j = pos, pos
        #     while i-1 > -1 and nums[i] == target and nums[i-1] == target:
        #         i-=1
        #     ans.append(i)
        #     while j+1 < len(nums) and nums[j] == target and nums[j+1] == target:
        #         j+=1
        #     ans.append(j)
        # return ans
        left = 0
        right = len(nums)
        ans = []
        pos = -1
        if nums == []:
            return [pos,pos]
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                pos = mid
                break
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        
        if pos == -1:
            return [-1,-1]
        i,j = pos, pos
        while i+1 < len(nums) and nums[i] == target and nums[i+1] == target:
            i += 1
        while j-1 > -1 and nums[j] == target and nums[j-1] == target:
            j -= 1
        ans.append(j)
        ans.append(i)
        return ans