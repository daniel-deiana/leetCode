# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isLeftValid(root, value):
    if root is None:
        return True
    
    return root.val < value and isLeftValid(root.left,value) and isLeftValid(root.right,value)

def isRightValid(root, value):
    if root is None:
        return True
    
    return root.val > value and isRightValid(root.left,value) and isRightValid(root.right,value)


class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        isLeftVld = isLeftValid(root.left,root.val)
        
        isRightVld = isRightValid(root.right,root.val)
        
        return isLeftVld and isRightVld and self.isValidBST(root.left) and self.isValidBST(root.right)
