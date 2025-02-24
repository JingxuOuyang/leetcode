from share import TreeNode
from typing import Optional
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        n = len(traversal)
        while i < n and traversal[i] != '-':
            i += 1
        
        root = TreeNode(int(traversal[0:i]))
        d1 = 0
        curNode = root
        stk = [root]
        while i < n:
            d2 = 0
            while traversal[i] == '-':
                d2 += 1
                i += 1
            j = i
            while i < n and traversal[i] != '-':
                i += 1
            nextNode = TreeNode(int(traversal[j:i]))
            
            if d2 == d1 + 1:
                stk[-1].left = nextNode
                stk.append(nextNode)
            else:
                while d1 != d2 - 1:
                    d1 -= 1
                    stk.pop()
                stk[-1].right = nextNode
                stk.append(nextNode)
            d1 = d2
            curNode = nextNode
        return root