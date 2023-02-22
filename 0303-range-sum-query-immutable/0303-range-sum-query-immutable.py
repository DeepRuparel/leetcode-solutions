class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ans = []
        sumTill = 0
        for i in nums:
            sumTill += i
            self.ans.append(sumTill)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left > 0 and right > 0:
            return self.ans[right] - self.ans[left - 1]
        else:
            return self.ans [left or right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)