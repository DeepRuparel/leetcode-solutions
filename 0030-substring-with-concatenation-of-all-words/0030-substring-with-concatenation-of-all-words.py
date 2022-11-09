class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        max_len = len(words)*len(words[0])
        # print(word)
        ans = []
        for i in range(len(s)-max_len+1):
            temp = s[i:i+max_len]
            
            sub = []
            for j in range(0,len(temp),len(words[0])):
                sub.append(temp[j:j+len(words[0])])
            
            if sorted(sub) == sorted(words):
                ans.append(i)
        return ans
                