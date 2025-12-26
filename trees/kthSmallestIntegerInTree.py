# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Push into a list the nodes, traversing the tree from
# Right to left and then return the -k th node from the top of the stack

def rightToLeftTraverse(root : Optional[TreeNode]):
    if root is None:
        return []
    
    return rightToLeftTraverse(root.right) + [root.val] +  rightToLeftTraverse(root.left)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return rightToLeftTraverse(root)[-k]
