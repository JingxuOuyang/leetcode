# Definition for a binary tree node.
#  class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from share import TreeNode
from typing import Optional, List
import sys
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        cur = list([root])
        ans = list([root.val])
        while len(cur) > 0:
            next = list([])
            maxValue = -(1 << 31)
            for node in cur:
                if node.left is not None:
                    next.append(node.left)
                    if node.left.val > maxValue:
                        maxValue = node.left.val
                if node.right is not None:
                    next.append(node.right)
                    if node.right.val > maxValue:
                        maxValue = node.right.val
            if len(next) > 0:
                ans.append(maxValue)
            cur = next
        return ans