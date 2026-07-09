# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rec(curr:Optional[TreeNode]):

    if curr is None:
        return 
    else:
        curr.right , curr.left = curr.left, curr.right
    
    rec(curr.left)
    rec(curr.right)



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        rec(root)

        return root 
        
     
