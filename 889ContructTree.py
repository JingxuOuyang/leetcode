from typing import List, Optional
from share import TreeNode
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def iterFunc(i1, j1, i2, j2):
            if i1 == j1:
                return TreeNode(preorder[i1])
            root = TreeNode(preorder[i1])
            leftChildRootVal = preorder[i1 + 1]
            i = i2
            while i <= j2 and postorder[i] != leftChildRootVal:
                i += 1
            leftChildLen = i - i2 + 1
            root.left = iterFunc(i1 + 1, i1 + leftChildLen, i2, i)
            if i != j2 - 1:
                root.right = iterFunc(i1 + leftChildLen + 1, j1, i + 1, j2 - 1)
            return root
        return iterFunc(0, len(preorder) - 1, 0, len(preorder) - 1)

s = Solution()
#root = (s.constructFromPrePost())
root = (s.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]))

#root = (s.constructFromPrePost(preorder = [1,2], postorder = [2,1]))
print(root.val)