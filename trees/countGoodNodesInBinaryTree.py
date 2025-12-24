# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def checkGoodNodes(root: TreeNode, path: list):
    if root is None:
        return 0

    isGood = 1 
    for nodeValue in path:
        isGood = 0 if nodeValue > root.val else isGood

    path = path + [root.val]
    return isGood + checkGoodNodes(root.left, path) + checkGoodNodes(root.right,path)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return checkGoodNodes(root,[root.val])
