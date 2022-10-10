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
        ans = len(d)
        
        for key,val in d.items():
            if val <= k:
                ans-=1
                k-=val
            else:
                break
        return ans
            
        
            
            