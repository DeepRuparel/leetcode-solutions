class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weakCharacters = 0
        maxDefense = 0
        # sort properties with custom sort comparator
        # if the attack is same, then sort defense in descending order  
        # otherwise, sort attack in in ascending order 
        properties.sort(key = lambda x: (x[0], -x[1]), reverse = True)
        for _, p in properties:
            if p < maxDefense:
                weakCharacters += 1
            else:
                maxDefense = p
        return weakCharacters
        
            
            
        