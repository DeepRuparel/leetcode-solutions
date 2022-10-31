class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        res = deque()
        
        right = bisect.bisect_left(arr, x)
        left = right - 1
        
        while left >= 0 and right < n and k > 0:
            left_delta = abs(x - arr[left])
            right_delta = abs(x - arr[right])
            if left_delta <= right_delta:
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])    
                right += 1
            k -= 1
        while k > 0:
            if left >= 0:
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1      
            k -= 1
        return res
                              