# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(root,max_val):
            if root is None:
                return 0

            count= 1 if max_val<=root.val else 0
            new_max=max(root.val,max_val)

            count+=traverse(root.left,new_max)
            count+=traverse(root.right,new_max)
            return count 


            
        
        return traverse(root,root.val)
            


        