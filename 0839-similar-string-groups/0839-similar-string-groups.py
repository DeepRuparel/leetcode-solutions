class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # a helper function to see if the two strings are similar or have differences at position 0 and 2
        
        def isSimilar(s1, s2):
            diffat0 = -1
            diffat2 = -1
            
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if diffat0 == -1:
                        diffat0 += 1
                    elif diffat2 == -1:
                        diffat2 += 1
                    else:
                        #more than two positions are different return False
                        return False
            # this means either o and 2 or different or nothing is different 
            return True
        
        # a list of list of str to save similar strings together
        groupedstrs = []
        
        for s in strs:
            curr_group = -1
            
            # if there are groups in groupedstrs we see if the current string can be placed in them
            for i, group in enumerate(groupedstrs):
                for s2 in group:
                    if isSimilar(s2, s):
                        #this is the first new string which can be found
                        if curr_group == -1:
                            # assign s to group i
                            groupedstrs[i].append(s)
                            #updating the curr_group since it is no longer the first one
                            curr_group = i
                            break
                        else:
                            groupedstrs[curr_group] = groupedstrs[curr_group] + groupedstrs[i]
                            del groupedstrs[i]
                            break
            #checking if this the first new string found append to list of strings for first pass and other non atching strings
            if curr_group == -1:
                groupedstrs.append([s])
        return len(groupedstrs)
                            
        
        
        
            
        