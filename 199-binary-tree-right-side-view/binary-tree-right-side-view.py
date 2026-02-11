# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]  

        def traverse(node,lvl):
            if node:
                if len(res)==lvl:
                    res.append(node.val)
                traverse(node.right,lvl+1)
                traverse(node.left,lvl+1)





        traverse(root,0)
        return res
