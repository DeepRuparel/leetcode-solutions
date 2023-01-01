class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            index = abs(nums[i])
            #print(index)
            if nums[index-1] < 0:
                ans.append(index)   
            else:
                nums[index-1] = -nums[index-1]
            i+=1
        return ans
            
                
        