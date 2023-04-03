class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        sort the people is ascending order
        then pop from front have capcity as 2 as yhou pop first one 
        decrease from limit the weight of the person popped if limit can still acomadte next person then 
        increase ans accordingly
        
        '''
        
        people = sorted(people)
        
        
        ### gave error since I was not handling the capacity the best way
        # neeed to be greed
        
        i = 0
        ans = 0
        j = len(people) - 1
        
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
                
        # i = len(people) - 1
        # ans = 0
        # while i >= 0:
        #     # sanity check to see if not empty
        #     temp = 0
        #     if people:
        #         person = people.pop(0)
        #         temp += 1
        #         # if people again a sanity check
        #         if people and person + people[0] <= limit and temp < 2:
        #             people.pop(0)
        #             temp += 1
        #             i -= temp
        #         else:
        #             i -= temp
        #         ans += 1
        # return ans
                    
                    
            