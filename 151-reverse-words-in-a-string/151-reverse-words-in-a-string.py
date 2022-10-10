class Solution:
    def reverseWords(self, s: str) -> str:
        #list_ofs = list(s)
        list_ofs = list(s.split())
        return " ".join(list_ofs[::-1])
        
            
        