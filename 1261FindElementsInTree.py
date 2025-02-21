from share import TreeNode
from typing import Optional

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        if target == 0:
            return self.root is not None
        binary_resprent = []
        target += 1
        while target > 0:
            binary_resprent.append(target % 2)
            target >>= 1
        node = self.root
        n = len(binary_resprent)
        for i in range(n - 2, -1, -1):
            if binary_resprent[i] == 0:
                node = node.left
            else:
                node = node.right
            if node is None:
                return False
        return True

f = FindElements()