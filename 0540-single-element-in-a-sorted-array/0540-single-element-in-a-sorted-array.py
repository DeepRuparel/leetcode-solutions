'''
One could see a pattern that [number, duplicate of the number have even and odd positions respectively].
if this pattern is broken meaning that is the element ehich has one single instance

so check for the condition if mid % 2 == 0 then is nums[mid + 1] also nums[mid]
or if mid % 2== 1 then is nums[mid - 1] == nums[mid] if yes condition is satisfied and it duplicate if present in left = mid+1 to right
else:
right = mid


'''
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0 
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) / 2
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]