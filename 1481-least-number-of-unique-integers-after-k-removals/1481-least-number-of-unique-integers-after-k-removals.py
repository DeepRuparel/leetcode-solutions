class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num = list()
        d = {}
        
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        d = dict(sorted(d.items(), key=lambda item: item[1]))
        nums = []
        for i in d.keys():
            nums.append(i)
        
        for i in range(k):
            n = nums[0]
            d[n] -= 1
            if d[n] == 0:
                d.pop(n)
                nums.pop(0)
        return len(nums)
            
        
            
            