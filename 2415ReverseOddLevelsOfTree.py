from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def transval(node:TreeNode, peerNode:TreeNode, level:int):
    if level % 2 == 1:
        t = node.val
        node.val = peerNode.val
        peerNode.val = t
    if node.left is not None:
        transval(node.left, peerNode.right, level + 1)
        transval(node.right, peerNode.left, level + 1)
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left is None:
            return root
        return transval(root.left, root.right, 1)