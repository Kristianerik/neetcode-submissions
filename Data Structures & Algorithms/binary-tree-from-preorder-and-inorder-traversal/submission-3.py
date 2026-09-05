# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: idx for idx, val in enumerate(inorder)}

        def build(preStart, inStart, inEnd):
            if preStart > len(preorder) - 1 or inStart > inEnd:
                return None

            mid = inorderMap[preorder[preStart]]
            root = TreeNode(preorder[preStart])
            leftSize = mid - inStart
            root.left = build(preStart + 1, inStart, mid - 1)
            root.right = build(preStart + leftSize + 1, mid + 1, inEnd)
            return root

        return build(0, 0, len(inorder) - 1)
    
    