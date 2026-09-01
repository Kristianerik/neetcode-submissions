# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        return self.dfs(root, root.val)

    def dfs(self, node: TreeNode, maxSoFar) -> int:
        if not node: return 0

        isGood = 1 if node.val >= maxSoFar else 0
        return isGood + self.dfs(node.left, max(maxSoFar, node.val)) + self.dfs(node.right, max(maxSoFar, node.val))