# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.flag = True

        def rec(curr: Optional[TreeNode]):

            if curr is None:
                return 0
            
            left = rec(curr.left)
            right = rec(curr.right)

            balanced = abs(left-right) <= 1

            if balanced is False:
                self.flag = balanced
            
            return 1 + max(left,right)
        
        result = rec(root)
        return self.flag


