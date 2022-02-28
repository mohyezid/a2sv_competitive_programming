# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d=1
        if not root:
            return 0
        def calc(root,d):
            if not root:
                return  d
            if root.left is None and root.right is None:
                return d
            else:
                return max(calc(root.left,d+1),calc(root.right,d+1))
        return calc(root,d)
        
