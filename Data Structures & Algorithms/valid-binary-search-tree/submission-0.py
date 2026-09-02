# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        return self.dfs(root, -math.inf, math.inf)
    
    def dfs(self, node: TreeNode, minVal, maxVal) -> bool:
        if not node: return True

        return (minVal < node.val < maxVal) and self.dfs(node.left, minVal, node.val) and self.dfs(node.right, node.val, maxVal)