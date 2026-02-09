# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len=0
        def dsf(root,goLeft,lng):
            nonlocal max_len
            if root is None:
                return
            
            max_len=max(max_len,lng)
            if goLeft:
                dsf(root.left,False,lng+1)
                dsf(root.right,True,1)
            else:
                dsf(root.right,True,lng+1)
                dsf(root.left,False,1)
        dsf(root,True,0)
        return max_len

        