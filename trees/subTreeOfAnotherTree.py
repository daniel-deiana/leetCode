# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            if p is None and q is None:
                return True
            elif p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False
            elif p.val != q.val:
                return False
            
            return True and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    
        if root is None:
            return False        

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
