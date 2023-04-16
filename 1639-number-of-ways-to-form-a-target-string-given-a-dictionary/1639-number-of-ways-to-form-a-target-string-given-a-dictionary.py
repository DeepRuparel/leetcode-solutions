class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        
        m = 10 ** 9 + 7
        
        dp = [1] + [0] * n
        
        for i in range(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in range(n, 0, -1):
                # if any target[j-1] re-appear in the current column distribution,
                # we need to check all previous dp[j] and add the total number of new `ways`
                # in addition to previous ways dp[j]
                dp[j] += dp[j-1] * count[target[j-1]] % m
        return dp[n] % m