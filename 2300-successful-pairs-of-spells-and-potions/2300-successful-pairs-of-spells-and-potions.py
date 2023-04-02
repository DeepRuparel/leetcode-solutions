class Solution:
    """
    Brute force : would be the way to go through every thing using a double for loops 
    complexity would be o(n*m)
    
    we need to find the minimum sterength pair, rest after that all are successful
    So we need to sort this
    and use binary search to get the minimum strength potion
    """
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def bsearch(i, potions):
            left = 0
            right = len(potions) - 1
            
            while left <= right:
                mid = left + ((right - left) // 2)
                if potions[mid] * i >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
                    
        potions = sorted(potions)
        ans = []
        for i in spells:
            k = bsearch(i, potions)
            #print(k)
            ans.append(len(potions) - k)
        return ans