class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        curr = self.d
        for l in word:
            if l not in curr:
                curr[l] = {}
            curr = curr[l]
        curr['#'] = {}
        

    def search(self, word: str) -> bool:
        def _search(word, trie):
            if not word:
                return '#' in trie
            if word[0] == '.':
                return any(_search(word[1:],v) for v in trie.values())
            if word[0] not in trie:
                return False
            return _search(word[1:],trie[word[0]])
        return _search(word,self.d)
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)