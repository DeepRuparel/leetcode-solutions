'''
Solution : Thinking of a dfs approach 
so 1st step to create a hashmap of courses and prerqs
so key: course to be taken values:prereqs is the courses need to be taken before that course

do a dfs on the courses and crate the soution backwards
in dfs there is a condition to see if the course in hashmap .keys if not you don't do anything
create a temp array to store the times of all the times and take the maximumof it since prereqs can be overlapped

Dry run:

1 -> 5 <- 2
      ^ ^
      |  \
      3-> 4
so lets say i = 1 
no key in hashmap go back
i = 2
no key in hashmap just return 
i =3 
no key in hashmap just return 
i = 4
key in hashmap
for the prereqs of course 4 
only 3 
time for 3 is 3 months
so add 3 to temp
return the temp
durataion for 4 would be max of temp hich is 3 + time for 3 so 7 months
now i = 5
key in hashmap
for the prereqs od course 5 
do a dfs(1)
append time to temp
do a dfs(2)
append time to temp
do a dfs(3) 
append time to temp
do a dfs(4)
for prereqs of 4 
only 3 do a dfs(3)
returns 3 + time for 4 = 7
append to temp 7
max of temp[1,2,3,7] + time for 5
so 7+5 = duration so 12 months 
return 12 months

to optimize this using memorization 
I would have a like a hashset of seen, if the course is seen just return the value from an array stored for that course or an dictionary
but array would work just fine as array[n-1] would be the time computed for the n course after dfs
so for the above example:
hashset would be {1,2,3,4}
and timecomputed array would be [1,2,3,7]
#update the array doesnot seem to work lets try a dictionary and elimainate the dhashset for lookup
'''
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # create a hashmap
        hashMap = {}
        for prereq, course in relations:
            if course in hashMap:
                hashMap[course].append(prereq)
            else:
                hashMap[course] = [prereq]
        #dictionary for all the course visisted and their respective times
        visisted = {}
        # minDuration = 0
        def dfs(course):
            # are we seeing the course fpr the first time?
            if course not in visisted:
                if course not in hashMap: # no prereq for the course we are seeing so, 
                                            #just add to self.visited the course and its duration
                    visisted[course] = time[course - 1]
                else:  # there exists a prereq
                    maxtime = 0
                    for prereq in hashMap[course]: #checking its prereq
                        if prereq not in visisted:
                            dfs(prereq)
                        maxtime = max(visisted[prereq], maxtime)
                    visisted[course] = maxtime + time[course - 1]
                    
        for i in range(1, n+1):
            dfs(i)
        maxtime = 0
        for i in visisted:
            maxtime = max(maxtime, visisted[i])
        return maxtime
        
        