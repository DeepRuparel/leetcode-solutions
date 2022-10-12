class Trie:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        curr = self.d
        for l in word:
            if l not in curr:
                curr[l] = {}
            curr = curr[l]
        curr['#'] = 1
        
    def search(self, word: str) -> bool:
        curr = self.d
        for l in word:
            if l not in curr:
                return False
            curr = curr[l]
        return '#' in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.d
        for l in prefix:
            if l not in curr:
                return False
            curr = curr[l]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)