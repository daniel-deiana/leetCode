# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []
        q = deque()
        nodesPerDepth = {}
        nodesPerDepth[0] = [root]
        q.append((root,0))
        while q:
            node, depth = q.popleft()
            if depth + 1 not in nodesPerDepth:
                nodesPerDepth[depth + 1] = []
            if node.left is not None:
                q.append((node.left, depth + 1))
                nodesPerDepth[depth + 1].append(node.left)
            if node.right is not None:
                q.append((node.right, depth + 1))
                nodesPerDepth[depth + 1].append(node.right)
        res = []
        for depth,nodes in nodesPerDepth.items():
            if len(nodes):
                res.append(nodes[-1].val)

        return res
