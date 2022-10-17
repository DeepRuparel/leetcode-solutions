class Solution:

    def __init__(self, w: List[int]):
        self.li = []
        ma = sum(w)
        
        for i, weight in enumerate(w):
            ratio = ceil(weight / ma * 100)
            self.li += ([i] * ratio)

    def pickIndex(self) -> int:
        return random.choice(self.li)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()