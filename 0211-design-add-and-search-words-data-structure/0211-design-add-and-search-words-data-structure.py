class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        d = self.d
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
        d['#'] = {}
                

    def search(self, word: str) -> bool:
        def _search(word, d):
            if not word:
                return '#' in d
            if word[0] == '.':
                return any(_search(word[1:], v) for v in d.values())
            if word[0] not in d:
                return False
            return _search(word[1:], d[word[0]])
        return _search(word, self.d)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)