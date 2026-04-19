# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = helper(node.left)
            right_depth = helper(node.right)

            self.best = max(self.best, right_depth + left_depth)
            return 1 + max(right_depth, left_depth)

        helper(root)
        return self.best
