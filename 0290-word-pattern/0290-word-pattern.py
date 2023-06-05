class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1={}
        d2={}
        for i in range(len(pattern)):
            if pattern[i] in d1:
                d1[pattern[i]]+=str(i)
            else:
                d1[pattern[i]]=str(i)
        l3=list(s.split(" "))
        for i in range(len(l3)):
            if l3[i] in d2:
                d2[l3[i]]+=str(i)
            else:
                d2[l3[i]]=str(i)
        l1=[]
        l2=[]
        for i in d1:
            l1.append(d1[i])
        for i in d2:
            l2.append(d2[i])
        if sorted(l1)!=sorted(l2):
            return False
            
        return True
        