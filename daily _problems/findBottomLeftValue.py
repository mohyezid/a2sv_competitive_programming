# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        
        temp = [] 
        q.append(root)
        
        while q:
            t = []
            for i in range(len(q)):
             
                node = q.popleft()
                res = node.val
                if node.left:
                    t.append(node.left.val)
                    q.append(node.left)
               
                if node.right:
                    q.append(node.right)
                    t.append(node.right.val)
            if t:
                temp.append(t)
        return temp[len(temp)-1][0] if temp else root.val
