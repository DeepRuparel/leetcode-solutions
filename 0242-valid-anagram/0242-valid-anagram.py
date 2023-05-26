class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        
        for i in s:
            s_dict[i] = 1 + s_dict.get(i,0)
        for i in t:
            t_dict[i] = 1 + t_dict.get(i,0)
        # s_dict = sorted(s_dict.items())
        # t_dict = sorted(t_dict.items())
        return s_dict == t_dict
        