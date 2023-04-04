class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        ans = 0
        for i in s:
            #print(seen)
            if i not in seen:
                seen.add(i)

            else:
                ans+=1
                seen = set()
                seen.add(i)
        return ans+1