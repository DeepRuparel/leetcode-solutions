class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        print(arr)
        if len(arr) == 1:
            return True
        diff = abs(arr[0] - arr[1])
        
        for i in range(1, len(arr)):
            curr_diff = abs(arr[i-1]- arr[i])
            if curr_diff != diff:
                return False
        return True
        