class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(s):
            if len(s)>3 or len(s)<1:
                return False
            if len(s)>1 and int(s) > 255:
                return False
            if len(s)>1 and s[0]=='0':
                return False
            
            return True
        ans = []
        for i in range(4):
            if not check(s[:i]):
                continue
            for j in range(i,i+4):
                if not check(s[i:j]):
                    continue
                for k in range(j,j+4):
                    if not check(s[j:k]):
                        continue
                    if not check(s[k:]):
                        continue
                    ans.append(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])
        return ans
                