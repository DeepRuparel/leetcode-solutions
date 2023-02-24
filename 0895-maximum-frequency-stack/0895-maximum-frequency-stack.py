class FreqStack(object):

    def __init__(self):
        self.stack = collections.Counter()
        self.maxList = collections.defaultdict(list)
        self.maxfreq = 0
    # def helper(self):
    #     maxfreq = {}
    #     for i in self.stack:
    #         if i not in maxfreq:
    #             maxfreq[i] = 1
    #         else:
    #             maxfreq[i] += 1
    #     if maxfreq != {}:
    #         m = max(maxfreq.items(), key=operator.itemgetter(1))[1]
    #         self.maxList = []
    #         for k, v in maxfreq.items():
    #             if v == m:
    #                 self.maxList.append(k)
        #print(self.maxList)
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        f = self.stack[val] + 1
        self.stack[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.maxList[f].append(val)

    def pop(self):
        """
        :rtype: int
        """
        ans = self.maxList[self.maxfreq].pop()
        self.stack[ans] -= 1
        if not self.maxList[self.maxfreq]:
            self.maxfreq -= 1
        return ans
#         self.helper()
#         ans = 0
#         if self.stack:
#             temp = self.stack[::-1]
#             index = len(temp) + 1
#             for item in self.maxList:
#                 curr_index = temp.index(item)
#                 index = min(curr_index, index)
#             ans = temp.pop(index)
#             self.stack = temp[::-1]
            
#         return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()