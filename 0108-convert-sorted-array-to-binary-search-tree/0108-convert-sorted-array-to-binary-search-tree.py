# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def tree(nums):
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = tree(nums[:mid])
            root.right = tree(nums[mid+1:])
            
            return root
        return tree(nums)
        
        