# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counter=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result=[]
        def check(arr):
            sum=0
            count=0
            for x in arr[::-1]:
                sum+=x
                if sum==targetSum:
                    count+=1
            return count
        def tree_traverse(root_node):
            if root_node is None:
                return 0
            result.append(root_node.val)
            tree_traverse(root_node.left)
            self.counter+=check(result)
            tree_traverse(root_node.right)
            result.pop()


            
        
        tree_traverse(root)

        return self.counter

        