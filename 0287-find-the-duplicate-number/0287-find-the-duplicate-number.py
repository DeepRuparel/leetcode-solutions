'''
Brute foce : make a hahsmap and check if ferequency 2 return that
or create a hashset if element already there means it is duplicate
Time : O(n)
size : O(n)

we want constant time and donot modify the array
hint : only 1 is duplicate and inclusive of 1 ... n

why not mark the array[i] go to the element arra[arra[i]] and check if already negative means was amrked by a duplivcate return array[i] if not mark it as negative

nums = [ 1, 3, 4, 2, 2]
        0   1   2  3 4   
i = 0 nums[0] = 1
check if nums[1] < 0 no
make it -3
nums = [1, -3, 4, 2, 2]
i = 1
arr[i] = -3 take abs of -3 = 3
if arr[3] < 0 no make it negative
nums = [1, -3, 4, -2, 2]
i = 2
arr[i] = 4 
check if array[4] < 0
no make it nergative
nums = [1, -3, 4, 2, -2]
i = 3
arr[i] = 2
check if arr[2] < 0 no make it negative
nums = [1, -3, -4, 2, -2]
i = 4
arr[i] = -2 abs(-2) = 2
check if arr[2] < 0 ? yes it is so ans = 2

make the array as orignal and return ans
space: o(1)
time: O(n)
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index] < 0:
                ans = index
                break
            nums[index] = -1 * nums[index]
        for i in range(len(nums)):
            nums[i] *= -1
        return ans