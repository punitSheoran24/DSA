# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result1=[]
        result2=[]
        def traverse(root,result):
            if root.left is None and root.right is None:
                result.append(root.val)
            if root.left is not None:
                traverse(root.left,result)
            if root.right is not None:
                traverse(root.right,result)
        
        traverse(root1,result1)
        traverse(root2,result2)

        return True if result1==result2 else False

