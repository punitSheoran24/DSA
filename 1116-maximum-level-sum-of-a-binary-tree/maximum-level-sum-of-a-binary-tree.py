# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque()
        queue.append(root)
        max_sum=float('-inf')
        level=0
        result=1

        while queue:
            level+=1
            qlen=len(queue)
            current_sum=0
            for i in range(qlen):
                node=queue.popleft()
                current_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_sum>max_sum:
                max_sum=current_sum
                result=level

        return result


       

         
        