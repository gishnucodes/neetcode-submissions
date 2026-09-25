# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashmap = defaultdict(list)
        self.traverse(root,hashmap,0)
        
        return list(hashmap.values())

    def traverse(self,root,hashmap,count):

        if root is None:
            return 
        else:
            hashmap[count].append(root.val)
            self.traverse(root.left,hashmap,count+1)
            self.traverse(root.right,hashmap,count+1)

